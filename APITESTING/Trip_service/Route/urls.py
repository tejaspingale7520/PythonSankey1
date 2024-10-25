from django.urls import path
from .views import route_details,route_list,access_day_night_times

urlpatterns = [
    path('route-listings/',route_list,name='route list'),
    path('route-details/<str:pk>/',route_details,name='route details'),
    path('date/',access_day_night_times,name='datetime')
  
   
]