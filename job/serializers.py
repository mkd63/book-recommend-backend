from rest_framework import serializers
from .models import Job
from . import models


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('id','url','company_name','role','start_date','end_date','currently_working','showcase','user')
