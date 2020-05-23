from rest_framework import serializers
from .models import Connections
from . import models

class ConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        fields = ('id', 'user1', 'user2', 'created_on')
