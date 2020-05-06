from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets, permissions
from .models import Interests
from .serializers import InterestsSerializer

# Create your views here.
class InterestsView(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
