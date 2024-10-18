from django.urls import path
from .views import get_book,update_book,create_book,delete_book,get_books,search
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('books/',get_books,name='get_book'),
    path('books/get/<int:pk>/',csrf_exempt(get_book),name='get_book_byid'),
    path('books/create/',csrf_exempt(create_book),name='create_book'),
    path('books/update/<int:pk>/',csrf_exempt(update_book),name='update_book'),
    path('books/delete/<int:pk>/',csrf_exempt(delete_book),name='delete_book'),
    path('books/search/',csrf_exempt(search),name='search book'),
]
