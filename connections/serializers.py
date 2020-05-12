from rest_framework import serializers
from .models import Connections
from . import models

class CollectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ('id', 'user1','user2')
