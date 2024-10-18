from django.urls import path
from .views import get_employee_details,get_employee,update_employee,create_employee,delete_employee,search_employee
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('getall/',get_employee_details,name='getallEmployee'),
    path('<int:pk>/',get_employee,name='getById'),
    path('update/<int:pk>/',csrf_exempt(update_employee),name='Updatedetails'),
    
    path('delete/<int:pk>/',csrf_exempt(delete_employee),name='deletedetails'),
    path('create/',csrf_exempt(create_employee),name='create employee'),
    path('search/',search_employee,name='search_employee')
]
