from rest_framework import serializers
from .models import Users
from . import models
from django.contrib.auth.hashers import make_password

class UsersSerializer(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields = ('id','username','email','first_name','last_name','password','dob','gender')


    def create(self, validated_data):
        user = models.Users(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=make_password(validated_data["password"]),
            dob=validated_data["dob"],
            gender=validated_data["gender"],
        )
        user.save()
        return user
