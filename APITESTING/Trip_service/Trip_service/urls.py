"""
URL configuration for Trip_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include

from Trip.views import trip_detail,trip_listing
from Route.views import route_details,route_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('route/',include('Route.urls')),
    path('trip/',include('Trip.urls')),
#     path('routes/',route_list,name='route listing'),
#     path('routes/<pk>/',route_details,name='route details'),
#     path('trips/',trip_listing,name='trip listing'),
#     path('trips/<pk>/',trip_detail,name='trip details'),
]
