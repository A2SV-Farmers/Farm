from rest_framework import generics
from .models import Farm, FarmImage
from .serializers import FarmSerializer, FarmImageSerializer



# Create View for Farm List 


class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FarmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


# Create View for Farm'image List 


class FarmImageListCreateView(generics.ListCreateAPIView):
    queryset = FarmImage.objects.all()
    serializer_class = FarmImageSerializer

class FarmImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmImage.objects.all()
    serializer_class = FarmImageSerializer
