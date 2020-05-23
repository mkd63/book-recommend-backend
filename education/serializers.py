from rest_framework import serializers
from .models import Education
from . import models

class EducatonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'institution_name', 'qualification_name', 'start_date', 'end_date', 'currently_studying', 'user', 'created_on')
