from django.db import models
from users.models import Users
# Create your models here.
class Connections(models.Model):

    user1 = models.IntegerField(blank=False)
    user2 = models.

    def __str__(self):
        return self.name
