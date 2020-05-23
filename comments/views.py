from rest_framework import viewsets
from .models import Comments
from .serializers import CommentsSerializer

class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
