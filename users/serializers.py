from rest_framework import serializers
from .models import Users
from . import models
from django.contrib.auth.hashers import make_password
from decouple import config
from django.utils.crypto import get_random_string
import hashlib, datetime
from django.core.mail import send_mail

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username','email','first_name','last_name','password','dob','gender','is_setup','picture','cropped_data')

    def create(self, validated_data):
        user = models.Users(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=make_password(validated_data["password"])
        )

        #We generate a random activation key
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = get_random_string(20, chars)
        verification_key = hashlib.sha256((secret_key + user.username).encode('utf-8')).hexdigest()
        user.verification_key = verification_key
        user.key_expires = datetime.datetime.now() + datetime.timedelta(days=2)
        user.save()

        subject = "Welcome " + user.first_name
        message = "Verify here: \n" + 'http://' + config('DOMAIN') + '/verify/' + verification_key

        send_mail(
            subject,
            message,
            "Devboat Team",
            [user.email]
        )

        return user
