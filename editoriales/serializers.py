from rest_framework import serializers
from .models import Editorial


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ("name", "address", "website", "city")