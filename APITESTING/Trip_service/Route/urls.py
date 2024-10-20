from django.urls import path
from .views import route_details,route_list

urlpatterns = [
    path('route-listings/',route_list,name='route list'),
    path('route-details/<str:pk>/',route_details,name='route details'),
   
]