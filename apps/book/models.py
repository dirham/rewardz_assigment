from django.db import models

class Book(models.Model):
    olid = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'