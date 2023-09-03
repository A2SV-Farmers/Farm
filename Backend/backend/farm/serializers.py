from rest_framework import serializers
from .models import Farm, FarmImage

# Farm Image Serializer

class FarmImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmImage
        fields = '__all__'

# Farm Serializer

class FarmSerializer(serializers.ModelSerializer):
    farm_images = FarmImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Farm
        fields = '__all__'
