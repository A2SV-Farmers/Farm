from django.db import models


# Product

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    certifications = models.TextField(blank=True, null=True)  # Certifications or quality standards
    reviews = models.JSONField(default=list)  # Field to store product reviews
    product_images = models.ManyToManyField('ProductImage', related_name='products')


    def __str__(self):
        return self.name


# Product image

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')

