from django.db import models
from users.models import Users

class Interests(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
