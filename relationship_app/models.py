from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.title)
class Library(models.Model):
    name = models.CharField(max_length=50, null=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return str(self.name)

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name