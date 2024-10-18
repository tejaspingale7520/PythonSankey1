from django.urls import path
from .views import item_list, item_create, item_detail, item_update, item_delete,item_partialupdate,login,RegisterAPI,LoginAPI

urlpatterns = [
    path('login/',login,name='login'),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('items/', item_list, name='item_list'),
    path('items/create/', item_create, name='item_create'),
    path('items/<int:pk>/', item_detail, name='item_detail'),
    path('items/update/<int:pk>/', item_update, name='item_update'),
    path('items/pupdate/<int:pk>/',item_partialupdate,name='partial_update'),
    path('items/delete/<int:pk>/', item_delete, name='item_delete'),
]
