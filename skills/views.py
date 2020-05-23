from rest_framework import viewsets
from .models import Skills
from .serializers import SkillsSerializer

class SkillsView(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
