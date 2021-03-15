from django.contrib.postgres.fields import ArrayField
from django.db import models
from users.models import Users

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = ArrayField(models.CharField(max_length=30, blank=True),size=8)
    genres = ArrayField(models.CharField(max_length=30, blank=True),size=8)
    picture = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    about_text = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name
