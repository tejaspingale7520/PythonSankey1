from django.urls import path
from .views import route_add,route_list,route_details

urlpatterns = [
    path('route-add/',route_add,name='route list'),
    path('route-listings/',route_list,name='route listings'),
     path('route-details/<pk>/',route_details,name='route details'),

]