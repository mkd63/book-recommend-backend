from rest_framework import viewsets
from .models import Upvotes
from .serializers import UpvotesSerializer

class UpvotesView(viewsets.ModelViewSet):
    queryset = Upvotes.objects.all()
    serializer_class = UpvotesSerializer
