from rest_framework.viewsets import ModelViewSet
from .serializers import EditorialSerializer
from .models import Editorial

# Create your views here.

class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer