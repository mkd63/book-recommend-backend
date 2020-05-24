from rest_framework import serializers
from .models import CommentUpvotes
from . import models

class CommentUpvotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentUpvotes
        fields = ('id', 'comment', 'user', 'created_on')
