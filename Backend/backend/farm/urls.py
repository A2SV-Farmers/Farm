from django.urls import path
from .views import FarmImageListCreateView, FarmImageDetailView, FarmListCreateView, FarmDetailView

urlpatterns = [

    # Farm urls

    path('farms/', FarmListCreateView.as_view(), name='farm-list-create'),
    path('farms/<int:pk>/', FarmDetailView.as_view(), name='farm-detail'),

    # FarmImage Detail 

    path('farmimages/', FarmImageListCreateView.as_view(), name='farmimage-create'),
    path('farmimages/<int:pk>/', FarmImageDetailView.as_view(), name='farmimage-detail'),

]
