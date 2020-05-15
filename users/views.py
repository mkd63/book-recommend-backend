from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Users
from .serializers import UsersSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
import cloudinary.uploader
import json

class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = "username"

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'list' or self.action == 'destroy' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]

    def partial_update(self, request, username):
        user = Users.objects.get(username=username)
        data = request.data.copy()
        file = data['picture']
        upload_data = cloudinary.uploader.upload(file)
        data['picture'] = json.dumps(upload_data)
        data['cropped_data'] = json.dumps(data['cropped_data'])

        serializer = UsersSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
