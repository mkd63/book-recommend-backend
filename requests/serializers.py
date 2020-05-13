from rest_framework import serializers
from .models import Requests
from . import models

class RequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requests
        fields = ('id', 'user1','user2','request_status')
