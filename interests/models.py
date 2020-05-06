from django.db import models
from users.models import Users
# Create your models here.
class Interests(models.Model):

    interest_name = models.CharField(max_length=100)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
