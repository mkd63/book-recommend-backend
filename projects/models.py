from django.db import models
from users.models import Users

class Projects(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    project_image = models.ImageField()
    active_token = models.BooleanField()
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
