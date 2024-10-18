from django.urls import path

from .views import get_users,create_user,delete_user,update_user

urlpatterns = [
    path('users/',get_users,name='get_users'),
    path('users/create/',create_user,name='create_user'),
   # path('users/<int:pk>',user_detail,name='user_details'),
    path('users/delete/<int:pk>/',delete_user,name='delete_user'),
    path('users/update/<int:pk>/',update_user,name='update_user')
    

  
]
