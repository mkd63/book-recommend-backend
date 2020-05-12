from rest_framework import serializers
from .models import Interests
from . import models

class InterestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interests
        fields = ('id','interest_name','user')
