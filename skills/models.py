from django.db import models
from users.models import Users
# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
