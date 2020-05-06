from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets, permissions
from .models import Education
from .serializers import EducatonSerializer

# Create your views here.
class EducationView(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducatonSerializer
