from rest_framework import serializers
from .models import Users
from . import models
from django.contrib.auth.hashers import make_password

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
            password=make_password(validated_data["password"]),
            dob=validated_data["dob"],
            gender=validated_data["gender"],
            is_setup=validated_data["is_setup"],
            picture=validated_data["picture"],
            cropped_data=validated_data["cropped_data"]
        )
        user.save()
        return user
