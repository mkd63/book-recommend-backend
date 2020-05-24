from rest_framework import viewsets
from .models import CommentUpvotes
from .serializers import CommentUpvotesSerializer

class CommentUpvotesView(viewsets.ModelViewSet):
    queryset = CommentUpvotes.objects.all()
    serializer_class = CommentUpvotesSerializer
