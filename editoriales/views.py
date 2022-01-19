from rest_framework.viewsets import ModelViewSet
from .serializers import EditorialSerializer
from .models import Editorial
from rest_framework.decorators import action
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer
from rest_framework import status
# Create your views here.

class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    @action(detail=True, methods=["GET"])
    def books(self, request, pk=None):
        editorial = self.get_object()
        books = Book.objects.filter(editorial__id=editorial.id)   
        serialized =BookSerializer(books, many=True)
        if not books:
            return Response(status=status.HTTP_404_NOT_FOUND, data={})
        return Response(status=status.HTTP_200_OK, data=serialized.data)