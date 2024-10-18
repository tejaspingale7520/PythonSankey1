from django.shortcuts import render
from django.http import JsonResponse
#from django.views.decorators.http import require_http_methods
#from django.views.decorators.http import require_http_methods
import json
from .models import Book



def get_books(request):
    books = Book.objects.all()
    # book_info=[]
    # for book in books:
    #   data = {"id": book.id, "title": book.title,"author": book.author, "published_date": str(book.published_date)}
    #   book_info.append(data)
    
    #using List comprehention
    book_info=[{"id": book.id, "title": book.title,"author": book.author, "published_date": str(book.published_date)} for book in books]
        
    return JsonResponse(book_info,safe=False)   ##to allow non dict data to serialize use safe=false

   # by id to get parameter
def get_book(request,pk):
    try:
        book = Book.objects.get(id=pk)
        data = {"id": book.id, 
                "title": book.title, 
                "author": book.author,
                  "published_date": str(book.published_date)}
        return JsonResponse(data)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


 ##to create data in table
def create_book(request):
    data = json.loads(request.body)
    book = Book.objects.create(title=data['title'],
                                author=data['author'], 
                                published_date=data['published_date'])
    return JsonResponse({'id': book.id}, status=201)



def update_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
        data = json.loads(request.body)
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.published_date = data.get('published_date', book.published_date)
        book.save()
        return JsonResponse({'id': book.id})

    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)
    
    

#to delete particular item
def delete_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
        return JsonResponse({'message': 'Book is deleted'}, status=204)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)

#search book name or by author name 
def search(request):
    
    query = request.GET.get('query', '')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__startswith=query)    ## you can serach with name
   
    # book_info = []
    # for book in books:
    #     data = {
    #         'title':book.title,
    #         'author':book.author,
    #         'published_date': book.published_date
    #     }
    #     book_info.append(data)

    book_info=[{'title':book.title,'author':book.author, 'published_date': book.published_date} for book in books]
    return JsonResponse(book_info,safe=False)

    
    


