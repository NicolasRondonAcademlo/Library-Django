
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name + " " + self.last_name 