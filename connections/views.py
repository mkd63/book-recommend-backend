from rest_framework import viewsets
from .models import Connections
from .serializers import ConnectionsSerializer

class ConnectionsView(viewsets.ModelViewSet):
    queryset = Connections.objects.all()
    serializer_class = ConnectionsSerializer
