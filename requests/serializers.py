from rest_framework import serializers
from .models import Requests
from . import models

class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'sender', 'receiver', 'request_status', 'created_on')
