from rest_framework import viewsets,status
from .models import Ratings
from books.models import Books
from users.models import Users
from .serializers import RatingsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.core import serializers
from django.http import HttpResponse
from .recommendations import recommend
from django.shortcuts import get_object_or_404


class RatingsView(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

    @action(detail=False,methods=["POST"], permission_classes=[IsAuthenticated])
    def user_book_rated(self, request):
        data = request.data.copy()

        users_books = Ratings.objects.select_related().filter(user_id=data["user_id"],book_id=data["book_id"])

        return_data = {}
        if len(users_books) > 0:
            data = serializers.serialize("json", users_books)
            return HttpResponse(data,status=status.HTTP_200_OK,content_type="application/json")
        else:
            return_data["status"] = False
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(True)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def recommendations(self, request, username=None):
        data = request.data.copy()
        user = get_object_or_404(Users, username=data["username"])
        users_books = Ratings.objects.filter(user_id=user.id).values()
        arr=[]
        for ub in users_books:
            book= Books.objects.get(id=ub.get("book_id"))
            arr.append((book.name,ub.get("rating")))

        recommended_data = recommend(user.id,arr)
        book_arr=[]
        for rb in recommended_data.keys().tolist():
            book= Books.objects.get(name=rb)
            book_arr.append(book)

        print(book_arr)
        serialized_data = serializers.serialize("json", book_arr)
        return HttpResponse(serialized_data,status=status.HTTP_200_OK,content_type="application/json")
