from rest_framework import viewsets, status,filters
from .models import Books
from .serializers import BooksSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'author', 'genres']

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'list' or self.action == 'destroy' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]

    @action(detail=False, permission_classes=[AllowAny])
    def books_rating(self, request):
        books = Books.objects.all().order_by('rating')
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, permission_classes=[AllowAny])
    def books_search(self, request):
        books = Books.objects.all().order_by('rating')
        data = request.data.copy()
        search_string = data['search_string']
        books = Books.objects.all().filter()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
