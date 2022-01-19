from statistics import mode
from django.db import models

# Create your models here.
class Editorial(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name