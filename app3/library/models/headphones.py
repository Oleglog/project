from django.db import models

class Headphones(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Headphone_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    

   