from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    reviews = models.JSONField(default=list)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title

