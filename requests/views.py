from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets, permissions
from .models import Requests
from .serializers import RequestsSerializer

# Create your views here.
class RequestsView(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
