from django.db import models
from users.models import Users

class Posts(models.Model):
    content = models.TextField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
