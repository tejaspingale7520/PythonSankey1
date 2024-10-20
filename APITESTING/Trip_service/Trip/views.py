
from django.shortcuts import render
# from django.http import JsonResponse,HttpResponse
# from .models import Trip
# #from .serializers import TripSerializer
# import json
# from django.core.exceptions import ValidationError

from django.http import JsonResponse,HttpResponse
from django.core.exceptions import ValidationError
import json
from Route.models import Route
from .models import Trip

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def trip_listing(request):
    if request.method == "GET":
        trips = Trip.objects.all()
        driver_name = request.GET.get('driver_name', None)
        if driver_name:
            trips = trips.filter(driver_name__icontains=driver_name)

        sort_by = request.GET.get('sort', None)
        if sort_by in ['trip_id', 'vehicle_id', 'user_id', 'driver_name']:
            trips = trips.order_by(sort_by)

        trip_data = [
            {'trip_id': trip.trip_id,
             'user_id': trip.user_id,
             'vehicle_id': trip.vehicle_id,
             'Route_id': {"Route_id":trip.Route_id.Route_id,"route_name":trip.Route_id.route_name,'route_origin':trip.Route_id.route_origin,'route_destination':trip.Route_id.route_destination,"route_stops":trip.Route_id.route_stops},
             'driver_name': trip.driver_name} for trip in trips
        ]
        
        return JsonResponse(trip_data, safe=False)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            route = Route.objects.get(Route_id=data['Route_id']) # "http://127.0.0.1:8000/route/route-listings/?Route_id=Route_id"
            #route = Route.objects.get(Route_id="http://127.0.0.1:8000/route/route-listings/")
            
            trip = Trip.objects.create(
                trip_id=data['trip_id'],
                user_id=data['user_id'],
                vehicle_id=data['vehicle_id'],
                Route_id=route,  
                driver_name=data['driver_name'])
            
            return JsonResponse({"id": trip.trip_id}, status=201)
        except ValidationError as ve:
            return JsonResponse({"errors": ve.messages}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def trip_detail(request, pk):
    try:
        trip = Trip.objects.get(trip_id=pk)
    except Trip.DoesNotExist:
        return JsonResponse({'error': 'Trip not found'}, status=404)

    if request.method == "GET":
        return JsonResponse({
            "trip_id": trip.trip_id,
            "user_id": trip.user_id,
            "vehicle_id": trip.vehicle_id,
            'Route_id': {"Route_id":trip.Route_id.Route_id,"route_name":trip.Route_id.route_name,'route_origin':trip.Route_id.route_origin,'route_destination':trip.Route_id.route_destination},
             "driver_name": trip.driver_name,"route_stops":trip.Route_id.route_stops
        },status=200)

    # elif request.method == 'POST':
    #     try:
    #         data = json.loads(request.body)
    #         trip = Trip.objects.create(**data)
    #         trip.save()
    #         return JsonResponse({"id": trip.id}, status=201)
    #     except ValidationError as ve:
   

    elif request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            # for key, value in data.items():
            #     setattr(trip, key, value)
            trip.trip_id=data.get('trip_id',trip.trip_id)
            trip.user_id=data.get('user_id',trip.user_id)
            trip.vehicle_id=data.get('vehicle_id',trip.vehicle_id)
            trip.Route_id=data.get('Route_id',trip.Route_id)
            trip.driver_name=data.get('driver_name',trip.driver_name)
            
            trip.full_clean()
            trip.save()
            return JsonResponse({"id": trip.trip_id,'message':'updated successfully'},status=200)
        except ValidationError as ve:
            return JsonResponse({"errors": ve.messages}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "DELETE":
        try:
            trip.delete()
            return HttpResponse({'msg':'deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

