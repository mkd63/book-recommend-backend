from rest_framework import serializers
from .models import Books
from . import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'name', 'author', 'genres', 'picture','about_text','rating', 'created_on')
