from django.db import models
from users.models import Users
# Create your models here.
class Requests(models.Model):

    user1 = models.ForeignKey(Users, related_name="receiver", null=True, on_delete=models.SET_NULL)
    user2 = models.ForeignKey(Users, related_name="sender", null=True, on_delete=models.SET_NULL)
    request_status = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.name
