from rest_framework import serializers
from .models import Comments
from . import models

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'content', 'post', 'user', 'created_on')
