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
