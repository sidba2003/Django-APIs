from django.db import models
from django.urls import reverse

class Author(models.Model):
    """Represents an author with a name, age, and active status."""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def as_dict(self):
        """Returns a dictionary representation of the author."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'active': self.active,
            'api': reverse('author api', args=[self.id])
        }

class Book(models.Model):
    """Represents a book with a title, description, authors, and publication date."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    authors = models.ManyToManyField(Author, through='Authorship', related_name='books')
    published = models.DateField()

    def __str__(self):
        return self.title

    def as_dict(self):
        """Returns a dictionary representation of the book, including authors with is_lead_author."""
        authorships = Authorship.objects.filter(book=self)
        authors_list = []
        for authorship in authorships:
            author_dict = authorship.author.as_dict()
            author_dict['is_lead_author'] = authorship.is_lead_author
            authors_list.append(author_dict)
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'authors': authors_list,
            'published': self.published,
            'api': reverse('book api', args=[self.id])
        }

class Authorship(models.Model):
    """Associates authors with books, indicating if they are lead authors."""
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_lead_author = models.BooleanField(default=False)

    def __str__(self):
        """Returns a string representation of the authorship."""
        return f"{self.author.name} - {self.book.title} ({'Lead' if self.is_lead_author else 'Co-author'})"
