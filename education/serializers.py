from rest_framework import serializers
from .models import Education
from . import models

class EducatonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Education
        fields = ('id','url', 'institution_name','qualification_name','start_date','end_date','currently_studying','user')
