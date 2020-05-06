from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets, permissions
from .models import Projects
from .serializers import ProjectsSerializer

# Create your views here.
class ProjectsView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
