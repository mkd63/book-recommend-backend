from rest_framework import viewsets
from .models import Projects
from .serializers import ProjectsSerializer

class ProjectsView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
