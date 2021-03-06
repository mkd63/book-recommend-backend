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
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
import datetime
import pytz
from django.utils.timezone import make_aware
from decouple import config
from django.utils.crypto import get_random_string
import hashlib
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from .recommendations import recommend

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        field = self.kwargs.get(self.lookup_field)
        filters = {}

        if field.isdigit():
            filters['pk'] = field
        else:
            filters['username'] = field

        obj = get_object_or_404(queryset, **filters)  # Lookup the object
        self.check_object_permissions(self.request, obj)  # check permissions.
        return obj

class UsersView(MultipleFieldLookupMixin, viewsets.ModelViewSet):
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

    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def recommendations(self, request, username=None):
        user = get_object_or_404(Users, username=username)

        data = recommend(user.username)

        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def admin(self, request):
        key="A2345918012"
        data = request.data.copy()
        dict={}
        if data["key"] == key:
            dict["success"] = True
        else:
            dict["success"] = False
        return Response(dict, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], permission_classes=[AllowAny])
    def set_picture(self, request, username=None):
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

    @action(detail=True, methods=['patch'], permission_classes=[AllowAny])
    def set_password(self, request, username=None):
        user = get_object_or_404(Users, username=username)
        user.password = make_password(request.data["password"])
        user.save()

        data = UsersSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def verify(self, request):
        verification_key = request.data['verification_key']

        user = get_object_or_404(Users, verification_key=verification_key)

        current_time = datetime.datetime.now()
        current_time = make_aware(current_time, pytz.UTC, False)

        if current_time > user.verification_key_expiry or user.is_verified:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            user.verification_key = None
            user.verification_key_expiry = None
            user.is_verified = True
            user.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def resend_verification_email(self, request):
        user = get_object_or_404(Users, username=request.data["username"])

        #We generate a random activation key
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = get_random_string(20, chars)
        verification_key = hashlib.sha256((secret_key + user.username).encode('utf-8')).hexdigest()
        user.verification_key = verification_key
        user.verification_key_expiry = datetime.datetime.now() + datetime.timedelta(days=2)

        subject = "Welcome " + user.first_name
        message = "Verify here: \n" + 'http://' + config('DOMAIN') + '/verify/' + verification_key

        send_mail(
            subject,
            message,
            "Devboat Team",
            [user.email]
        )

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def send_reset_password_email(self, request):
        user = get_object_or_404(Users, email=request.data["email"])

        #We generate a random activation key
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = get_random_string(20, chars)
        reset_password_key = hashlib.sha256((secret_key + user.username).encode('utf-8')).hexdigest()
        user.reset_password_key = reset_password_key
        user.reset_password_key_expiry = datetime.datetime.now() + datetime.timedelta(days=2)
        user.save()

        subject = "Welcome " + user.first_name
        message = "Reset password here: \n" + 'http://' + config('DOMAIN') + '/reset/' + reset_password_key

        send_mail(
            subject,
            message,
            "My Books Team",
            [user.email]
        )

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def reset(self, request):
        reset_password_key = request.data['reset_password_key']

        user = get_object_or_404(Users, reset_password_key=reset_password_key)
        current_time = datetime.datetime.now()
        current_time = make_aware(current_time, pytz.UTC, False)

        data = UsersSerializer(user).data

        if current_time > user.reset_password_key_expiry:
            print("expired") # TODO: return valid Response
        else:
            return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def reset_done(self, request):
        reset_password_key = request.data['reset_password_key']

        user = get_object_or_404(Users, reset_password_key=reset_password_key)
        user.reset_password_key = None
        user.reset_password_key_expiry = None
        user.save()

        return Response(status=status.HTTP_200_OK)
