from rest_framework import serializers
from .models import Job
from . import models

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company_name', 'role', 'start_date', 'end_date', 'currently_working', 'user', 'created_on')
