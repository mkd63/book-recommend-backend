from rest_framework import serializers
from .models import Skills
from . import models

class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ('id','skill_name','skill_level','user')
