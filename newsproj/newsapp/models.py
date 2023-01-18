from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Article(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=50, unique=True, )
    description = models.TextField()
    author = models.ForeignKey('Author', null=True, on_delete=models.PROTECT)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.title()
