from django.shortcuts import render
from .models import Routing
import json
from django.http import JsonResponse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def route_list(request):
   
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            route = Routing.objects.create(
                Route_id=data['Route_id'],
                user_id=data['user_id'],
                route_name=data['route_name'],
                route_origin=data['route_origin'],
                route_destination=data['route_destination'],
                route_stops=data['route_stops']
            )
            
            route.full_clean()
            route.save()
            return JsonResponse({"record inserted for id": route.Route_id}, status=201)
        except IntegrityError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
