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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from dateutil import parser

@csrf_exempt
def access_day_night_times(request):
    if request.method == 'POST':
        try:
            # Load the incoming JSON data
            data = json.loads(request.body)
            
            # Use dateutil.parser to parse the dates
            start_date = parser.parse(data['start_date'])
            end_date = parser.parse(data['end_date'])
 
            night_times = []
            day_times = []
 
            current_date = start_date
 
            while current_date < end_date:
                night_start = current_date.replace(hour=21, minute=0, second=0)
                night_end = current_date.replace(hour=6, minute=0, second=0) + timezone.timedelta(days=1)
 
                if night_end > end_date:
                    night_end = end_date

                night_times.append({
                    "start_date": night_start.isoformat(),
                    "end_date": night_end.isoformat()
                })

                day_start = night_end
                day_end = day_start + timezone.timedelta(days=1)

                if day_end > end_date:
                    day_end = end_date

                day_times.append({
                    "start_date": day_start.isoformat(),
                    "end_date": day_end.isoformat()
                })

                current_date += timezone.timedelta(days=1)
 
            return JsonResponse({
                "night_time": night_times,
                "day_time": day_times
            })
 
        except (json.JSONDecodeError, KeyError, ValueError):
            return JsonResponse({"error": "Invalid request data"}, status=400)
 
    return JsonResponse({"error": "Method not allowed"}, status=405)

#input json
# {
   
#     "start_date": "2023-10-22T15:30:00",
#     "end_date": "2023-10-23T15:30:00"
# }

##output response
# {
#     "night_time": [
#         {
#             "start_date": "2023-10-22T21:00:00",
#             "end_date": "2023-10-23T06:00:00"
#         }
#     ],
#     "day_time": [
#         {
#             "start_date": "2023-10-23T06:00:00",
#             "end_date": "2023-10-23T15:30:00"
#         }
#     ]
# }
    


