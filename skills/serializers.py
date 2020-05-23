from rest_framework import serializers
from .models import Skills
from . import models

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ('id', 'name', 'level', 'user', 'created_on')
