from django.db import models
from users.models import Users
# Create your models here.
class Requests(models.Model):
    sender = models.ForeignKey(Users, related_name="sender", null=True, on_delete=models.SET_NULL)
    receiver = models.ForeignKey(Users, related_name="receiver", null=True, on_delete=models.SET_NULL)
    request_status = models.IntegerField(null=True,default=0)

    class Meta:
        unique_together = ["sender", "receiver"]

    def __str__(self):
        return self.name
