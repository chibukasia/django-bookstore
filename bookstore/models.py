from django.db import models

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Book author")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title 

    class Meta:
        ordering = ['title', 'created']