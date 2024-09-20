from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self) -> str:
        return self.title
