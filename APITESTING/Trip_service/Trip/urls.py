from django.urls import path
from .views import trip_listing,trip_detail

urlpatterns = [
    path('trip-listings/',trip_listing,name='trip list'),
    path('trip-details/<str:pk>/',trip_detail,name='trip details'),
   
]