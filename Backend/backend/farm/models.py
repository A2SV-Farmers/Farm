from django.db import models
from product.models import Product  

# Farm

class Farm(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    practice_description = models.TextField()
    farm_images = models.ManyToManyField('FarmImage', related_name='farms')  # ManyToMany relationship with FarmImage
    products = models.ManyToManyField(Product, related_name='farms',blank=True)
    
    def __str__(self):
        return self.name

# Farm's Image

class FarmImage(models.Model):
    image = models.ImageField(upload_to='farm_images/')



