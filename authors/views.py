from os import stat
from books.models import Book
from books.serializers import BookSerializer
from .models import Author
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=["GET"])
    def books(self, request, pk=None):
        author = self.get_object()
        books = Book.objects.filter(authors__id=author.id)
        serialized = BookSerializer(books, many=True)
        if not books:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "message": "Este autro no tiene libros"
                }
            )
        return Response(status=status.HTTP_200_OK, data=serialized.data)