from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CharField, null=True, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    time_required = models.CharField(max_length=30)
    instructions = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
