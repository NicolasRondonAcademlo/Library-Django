from http import server
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authors.models import Author
from authors.serializers import AuthorSerializer
from books.models import Book
from books.serializers import BookSerializer, BookCreateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return BookCreateSerializer
        return BookSerializer

    @action(detail=True, methods=['GET'])
    def authors(self, request, pk=None):
        book = self.get_object()
        authors = Author.objects.filter(book__id=book.id)
        serialized = AuthorSerializer(authors, many=True)
        if not authors:
            return Response(status=status.HTTP_404_NOT_FOUND,
            data={
                "message": "This book doesn't have authors"
            })
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=["GET"])
    def editorial(self, request, pk=None):
        book = self.get_object()
        editorial = Editorial.objects.filter(book__id=book.id)
        serialized = EditorialSerializer(editorial, many=True)
        if not editorial:
            return Response(status=status.HTTP_404_NOT_FOUND,
            data={
                "message": "This book doesn't have editorial"
            })
        return Response(status=status.HTTP_200_OK, data=serialized.data)