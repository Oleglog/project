from django.db import models

# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=10)
    year = models.CharField(max_length=4)

class Author (models.Model):
    name = models.CharField(max_length=10)
    date_of_birth = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)