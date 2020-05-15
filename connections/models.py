from django.db import models
from users.models import Users
# Create your models here.
class Connections(models.Model):

    user1 = models.ForeignKey(Users, related_name="user1", null=True, on_delete=models.SET_NULL)
    user2 = models.ForeignKey(Users, related_name="user2", null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ["user1", "user2"]

    def __str__(self):
        return self.name
