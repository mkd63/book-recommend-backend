from rest_framework import viewsets
from .models import Interests
from .serializers import InterestsSerializer

class InterestsView(viewsets.ModelViewSet):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
