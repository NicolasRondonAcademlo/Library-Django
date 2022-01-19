from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorSerializer
from editoriales.serializers import EditorialSerializer

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    editorial = EditorialSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'editorial', 'date_pub', 'id')

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'editorial' )