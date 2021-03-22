from rest_framework import serializers
from .models import Ratings
from . import models

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'user', 'book','rating', 'created_on')
