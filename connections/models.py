from django.db import models
from users.models import Users

class Connections(models.Model):
    user1 = models.ForeignKey(Users, related_name="user1", null=True, on_delete=models.SET_NULL)
    user2 = models.ForeignKey(Users, related_name="user2", null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ["user1", "user2"]

    def __str__(self):
        return self.name
