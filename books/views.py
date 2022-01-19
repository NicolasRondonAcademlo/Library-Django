from http import server
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.serializers import BookSerializer, BookCreateSerializer
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return BookCreateSerializer
        return BookSerializer