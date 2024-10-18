
from django.urls import path
from .views import create_cart,get_cart_details,get_item,update_item,delete_item,update_itempartial,search_item,search_itemsorder
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
   path('create/',csrf_exempt(create_cart),name='create item '),
   path('',get_cart_details,name='get all cart details'),
   path('<int:pk>/',get_item,name='get by id'),
   path('update/<int:pk>/',csrf_exempt(update_item),name='update cart'),
   path('pupdate/<int:pk>/',csrf_exempt(update_itempartial),name='partial update'),
   path('delete/<int:pk>/',csrf_exempt(delete_item),name='delete item'),
   path('search/',csrf_exempt(search_item),name='search items'),
   path('search-order/',csrf_exempt(search_itemsorder),name='serach by order des')


]