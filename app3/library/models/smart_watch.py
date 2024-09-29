from django.db import models

class Smart_watch(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Smart_watch_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    