from rest_framework import serializers
from .models import Skills
from . import models

class SkillsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skills
        fields = ('id','url','skill_name','skill_level','user')
