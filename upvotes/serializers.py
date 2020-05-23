from rest_framework import serializers
from .models import Upvotes
from . import models

class UpvotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvotes
        fields = ('id', 'post', 'user', 'created_on')
