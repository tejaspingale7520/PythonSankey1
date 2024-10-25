from django.urls import path
from .views import booking_add,booking_listing,booking_detail

urlpatterns = [
    path('booking-add/', booking_add, name='booking-list'),
    path('booking-listings/', booking_listing, name='booking-listings'),
    path('booking-details/<pk>/', booking_detail, name='booking-details'),
    
]