from rest_framework import serializers
from .models import Projects
from . import models

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Projects
        fields = ('id','name','description','project_image','active_token','user')
