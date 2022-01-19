from statistics import mode
from django.db import models
from authors.models import Author
from editoriales.models import Editorial
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now())

    def __str__(self) -> str:
        return self.title