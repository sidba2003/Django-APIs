from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'active': self.active,
            'api': reverse('author api', args=[self.id])
        }



class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ManyToManyField(Author, through='Authorship')
    published = models.DateField()

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            'title': self.title,
            'author': self.author.as_dict(),
            'published': self.published,
            'api': reverse('book api', args=[self.id])
        }


class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_lead_author = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"
