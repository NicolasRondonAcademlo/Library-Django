from .models import Author
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer