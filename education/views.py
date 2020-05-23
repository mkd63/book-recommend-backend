from rest_framework import viewsets
from .models import Education
from .serializers import EducatonSerializer

class EducationView(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducatonSerializer
