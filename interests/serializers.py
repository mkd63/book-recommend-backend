from rest_framework import serializers
from .models import Interests
from . import models

class InterestsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Interests
        fields = ('id','url','interest_name','user')
