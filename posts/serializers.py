from rest_framework import serializers
from .models import Posts
from . import models

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'content', 'picture', 'user', 'created_on')
