from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 100, blank=False, unique=True)
    email = models.EmailField(max_length = 100, blank=False)
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, default='',blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    gender = models.CharField(null=True,max_length = 10,blank=True)
    is_setup = models.IntegerField(null=True,default=0)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=["first_name"])]

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
