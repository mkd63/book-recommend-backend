from rest_framework import serializers
from .models import Books
from . import models
import cloudinary.uploader
import json

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'name', 'author', 'genres', 'picture','cropped_data','google_link','about_text','rating', 'created_on')

    def create(self, validated_data):
        file = validated_data['picture']
        upload_data = cloudinary.uploader.upload(file)
        print(validated_data['cropped_data'])
        book = models.Books(
            name=validated_data["name"],
            author=validated_data["author"],
            genres=validated_data["genres"],
            about_text=validated_data["about_text"],
            rating=validated_data["rating"],
            google_link=validated_data["google_link"],
            picture = json.dumps(upload_data),
            cropped_data = validated_data['cropped_data']
        )

        book.save()
        return book
