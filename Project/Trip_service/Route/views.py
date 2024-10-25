from django.shortcuts import render
import json
from .models import Route
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# Create your views here.
@csrf_exempt
def route_add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            route = Route.objects.create(
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
@csrf_exempt
def route_list(request):
    if request.method == "GET":
        routes = Route.objects.all()#receives data from model

        # paginator=Paginator(routes,10)#setting limits to get 2 records
        # page_number=request.GET.get('page')#getting page number from url  default is 1
        # routes_data=paginator.get_page(page_number)# depending upon page number which data will come

        
        route_name_query = request.GET.get('route_name', None)
        if route_name_query:
            routes = routes.filter(route_name__icontains=route_name_query)
        
        Route_id_query=request.GET.get('Route_id',None)
        if Route_id_query:
            routes=routes.filter(Route_id__icontains=Route_id_query)
        
        # Sorting
        sort_by = request.GET.get('sort_by', None)
        if sort_by in ['route_origin', 'route_destination', 'route_name','user_id' ,'Route_id']:
            routes = routes.order_by(sort_by)
        
        
        data = [ {"Route_id": route.Route_id,
        "user_id": route.user_id,
        "route_name": route.route_name,
        "route_origin": route.route_origin,
        "route_destination": route.route_destination,
        "route_stops": route.route_stops if route.route_stops else []}for route in routes]
        
        return JsonResponse(data, safe=False)
    
@csrf_exempt
def route_details(request,pk):
    try:
        route = Route.objects.get(Route_id=pk)
    except Route.DoesNotExist:
        return JsonResponse({'error': 'Route not found'}, status=404)
    
    if request.method == "GET":

        return JsonResponse({
            "Route_id": route.Route_id,
            "user_id": route.user_id,
            "route_name": route.route_name,
            "route_origin": route.route_origin,
            "route_destination": route.route_destination,
            "route_stops": route.route_stops
        }, status=200)
    
    elif request.method =='PUT' or request.method== 'PATCH':
        try:
            data = json.loads(request.body)

            # for key, value in data.items():
            #     setattr(route, key, value)
            route.Route_id=data.get('Route_id',route.Route_id)
            route.user_id=data.get('user_id',str(route.user_id))
            route.route_name=data.get('route_name',route.route_name)
            route.route_origin=data.get('route_origin',route.route_origin)
            route.route_destination=data.get('route_destination',route.route_destination)
            route.route_stops=data.get('route_stops',route.route_stops)

            route.full_clean()
            route.save()

            return JsonResponse({"id": route.Route_id},status=200)
        except ValidationError as ve:
            return JsonResponse({"errors": ve.messages}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    
    
    elif request.method == "DELETE":

        
        route.delete()
        return JsonResponse({'message': "Route deleted"}, status=200)
   