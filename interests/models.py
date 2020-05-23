from django.db import models
from users.models import Users

class Interests(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
