from django.db import models
from users.models import Users

class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
