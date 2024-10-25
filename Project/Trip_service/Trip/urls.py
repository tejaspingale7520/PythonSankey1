from django.urls import path
from .views import trip_add,trip_listing,trip_detail

urlpatterns = [
    path('trip-add/',trip_add,name='trip add'),
    path('trip-listings/',trip_listing,name='trip listing'),
    path('trip-details/<pk>/',trip_detail,name='trip listing'),
   
   
]