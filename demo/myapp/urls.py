from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("todos/",views.todos, name="Todos"),
    path('fetch-kakiz/',views.fetch_data_from_kakiz,name='interservice call')

   
]