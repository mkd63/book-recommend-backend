from rest_framework import viewsets
from .models import Requests
from .serializers import RequestsSerializer

class RequestsView(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
