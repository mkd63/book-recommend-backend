from rest_framework import viewsets, status,filters
from .models import Books
from .serializers import BooksSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Users
from django.shortcuts import get_object_or_404

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


    @action(detail=False, permission_classes=[IsLoggedInUserOrAdmin])
    def books_genre_recommendation(self, request, username=None):
        books = Books.objects.all().order_by('rating')
        user = get_object_or_404(Users, username=request.query_params.get('username').split("/")[0])
        recommended_books = [];
        for i in user.preferred_genres:
            for j in books:
                if i in j.genres:
                    if j not in recommended_books:
                        recommended_books.append(j)

        serializer = self.get_serializer(recommended_books, many=True)
        #serializer = self.get_serializer(recommended_books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['patch'],permission_classes=[IsAuthenticated])
    def books_rating_patch(self, request):
        data = request.data.copy()
        book = get_object_or_404(Books, id=data["id"])

        book.rating = (data["rating"] + book.rating)/2
        book.save()
        rating_data = BooksSerializer(book).data
        dict = {}
        dict["auth"] = "Not authenticated"
        if data["token"]:
            return Response(rating_data, status=status.HTTP_200_OK)
        else:
            return Response({"auth": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)    
