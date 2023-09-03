from rest_framework import serializers
from .models import Product, ProductImage


# Product's Image Serializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


# Product Image Serializer


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
