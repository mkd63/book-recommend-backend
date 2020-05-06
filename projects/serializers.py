from rest_framework import serializers
from .models import Projects
from . import models

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id','name','description','project_image','active_token','user')
