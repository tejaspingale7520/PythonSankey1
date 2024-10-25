from django.urls import path
from .views import route_list

urlpatterns = [
    path('route-listings/',route_list,name='route list'),
   
   
]