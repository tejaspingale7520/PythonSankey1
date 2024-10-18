from django.shortcuts import render,HttpResponse
from .models import ToDoItem
import requests,json
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,"home.html")


def todos(request):
    items = ToDoItem.objects.all()
    return render(request,"todos.html",{"todos":items})

#url="http://127.0.0.1:9000/api/users/"
def fetch_data_from_kakiz(url):
    req=requests.get("http://127.0.0.1:9000/api/users/")
    data=req.json()
    return JsonResponse(data,safe=False)
    
