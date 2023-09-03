from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductImageListCreateView, ProductImageDetailView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('productimages/', ProductImageListCreateView.as_view(), name='productimage-create'),
    path('productimages/<int:pk>/', ProductImageDetailView.as_view(), name='productimage-detail'),
]
