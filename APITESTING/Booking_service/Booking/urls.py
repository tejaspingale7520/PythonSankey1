
from django.urls import path
from .views import booking_listing,booking_detail

urlpatterns = [
    path('booking-listings/', booking_listing, name='booking-list'),
    path('booking-details/<str:pk>/', booking_detail, name='booking-detail'),
    
]