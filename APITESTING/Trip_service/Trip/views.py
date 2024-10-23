from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError
import json
import requests
from Route.models import Route
from .models import Trip
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core.paginator import Paginator
from .middleware import UserAccessPermission
from django.core.paginator import Paginator
# from requests.auth import HTTPBasicAuth

# @csrf_exempt

# def trip_listing(request):

#     try:
#         if request.method == "GET":
#             # Fetching trips
#             trips = Trip.objects.all()
            

#             # Implementing search functionality
#             driver_name_query = request.GET.get('driver_name', None)
#             if driver_name_query:
#                 trips = trips.filter(driver_name__icontains=driver_name_query)

#             # Implementing sorting functionality
#             sort_by = request.GET.get('sort', None)
#             if sort_by in ['trip_id', 'vehicle_id', 'user_id', 'driver_name']:
#                 trips = trips.order_by(sort_by)

#             # Fetch Bookings from the BookingService
#             booking_service_url = 'http://127.0.0.1:9000/api/booking-listings/'
#             # Use Basic Auth for the request
#             # response = requests.get(booking_service_url, auth=HTTPBasicAuth('username', 'password'))
#             # response = requests.get(booking_service_url)
#             response = requests.get(booking_service_url, auth=('admin','superuser'))
            
#             if response.status_code == 200:
#                 bookings = response.json()
#                 data = []
#                 for trip in trips:
#                     booking_info = next((booking for booking in bookings if  booking['trip_id'] == trip.trip_id), None)
#                     data.append({
#                         'trip_id': trip.trip_id,
#                         'user_id': trip.user_id,
#                         'vehicle_id': trip.vehicle_id,
#                         'Route_id': {
#                             "Route_id": trip.Route_id.Route_id,
#                             "route_name": trip.Route_id.route_name,
#                             'route_origin': trip.Route_id.route_origin,
#                             'route_destination': trip.Route_id.route_destination,
#                             "route_stops": trip.Route_id.route_stops
#                         },
#                         'driver_name': trip.driver_name,
#                         'booking_info': booking_info
#                     })
#                 return JsonResponse(data, safe=False)
            
#             else:
#                 return JsonResponse({'error': 'Unable to fetch bookings'}, status=response.status_code)
            
#         elif request.method == 'POST':
#                     data = json.loads(request.body)
                    
#                     booking_service_url = f'http://127.0.0.1:9000/api/booking-listings/?search={data.get('trip_id')}'
#                             # booking_response = requests.get(booking_service_url, auth=HTTPBasicAuth('username', 'password'))
#                     booking_response = requests.get(booking_service_url, auth=('admin', 'superuser'))
#                     print(booking_response)
#                     # print("************",booking_response)
#                     # trip_id_res = booking_response["trip_id"

#                     if booking_response.status_code == 200:
#                         resData = booking_response.json()
#                         print(resData)
#                         return JsonResponse({"booking data": resData}, status=201)
#                     else:
#                         return JsonResponse({"error": "Booking not found"}, status=404)

#     # except Exception as e:
#     #         return JsonResponse({"error": str(e)}, status=500)
#     # except ValidationError as ve:
#     #         return JsonResponse({"errors": str(ve)}, status=400)
#     # except json.JSONDecodeError:
#     #         return JsonResponse({"error": "Invalid JSON"}, status=400)
#     except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
    

# @csrf_exempt
# def trip_detail(request, pk):
#     try:
#         trip = Trip.objects.get(trip_id=pk)
#     except Trip.DoesNotExist:
#         return JsonResponse({'error': 'Trip not found'}, status=404)

#     booking_service_url = f'http://127.0.0.1:9000/api/booking-details/{pk}/'

#     if request.method == "GET":
#         booking_response = requests.get(booking_service_url)

#         if booking_response.status_code == 200:
#             booking_info = booking_response.json()
#             print(booking_info)
#             return JsonResponse({
#                 "trip_id": trip.trip_id,
#                 "user_id": trip.user_id,
#                 "vehicle_id": trip.vehicle_id,
#                 "Route_id": {
#                     "Route_id": trip.Route_id.Route_id,
#                     "user_id": trip.Route_id.user_id,
#                     "route_name": trip.Route_id.route_name,
#                     "route_origin": trip.Route_id.route_origin,
#                     "route_destination": trip.Route_id.route_destination,
#                     "route_stops": trip.Route_id.route_stops
#                 },
#                 "driver_name": trip.driver_name,
#                 "booking_info": booking_info
#             }, status=200)
#         else:
#             return JsonResponse({"error": "Booking details not found"}, status=booking_response.status_code)

#     elif request.method in ['PUT', 'PATCH']:
#         try:
#             data = json.loads(request.body)
#             trip.trip_id = data.get('trip_id', trip.trip_id)
#             trip.user_id = data.get('user_id', trip.user_id)
#             trip.vehicle_id = data.get('vehicle_id', trip.vehicle_id)
#             trip.Route_id = Route.objects.get(Route_id=data.get('Route_id', trip.Route_id))
#             trip.driver_name = data.get('driver_name', trip.driver_name)

#             trip.full_clean()
#             trip.save()
#             return JsonResponse({"id": trip.trip_id, 'message': 'Updated successfully'}, status=200)
#         except ValidationError as ve:
#             return JsonResponse({"errors": ve.messages}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     elif request.method == "DELETE":
#         try:
#             trip.delete()
#             return JsonResponse({'msg': 'Deleted successfully'}, status=200)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)





















# from django.shortcuts import render
# # from django.http import JsonResponse,HttpResponse
# # from .models import Trip
# # #from .serializers import TripSerializer
# # import json
# # from django.core.exceptions import ValidationError

from django.http import JsonResponse,HttpResponse
from django.core.exceptions import ValidationError
import json,requests
from Route.models import Route
from .models import Trip

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# @UserAccessPermission
def trip_listing(request):
    if request.method == "GET":
        trips = Trip.objects.all()

        # paginator=Paginator(trips,5)#setting limits to get 2 records
        # page_number=request.GET.get('page')#getting page number from url  default is 1
        # trips_data=paginator.get_page(page_number)# depending upon page number which data will come

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
             'driver_name': trip.driver_name} for trip in trips]
        return JsonResponse(trip_data, safe=False)
    
    elif request.method == 'POST':
            try:
                data = json.loads(request.body)
                trip = Trip.objects.create(**data)
                trip.save()
                return JsonResponse({"id": trip.id}, status=201)
            except ValidationError as ve:
                  return JsonResponse({"error": str(ve)}, status=500)
    
    
#     if request.method == "GET":
#         # Fetch Bookings from the BookingService
#         booking_service_url = 'http://127.0.0.1:9000/api/booking-listings/'  
#         response = requests.get(booking_service_url)
#         # print(response)
#         if response.status_code == 200:
#             bookings = response.json()  # Get trip data
#             #print(bookings)
#             # Prepare booking data along with trip information
#             trips = Trip.objects.all()
#             data = []
#             for trip in trips:
#                 booking_info = next((booking for booking in bookings if booking['trip_id'] == trip.trip_id), None)
#                 data.append({
#                     'trip_id': trip.trip_id,
#                     'user_id': trip.user_id,
#                     'vehicle_id': trip.vehicle_id,
#                     'Route_id': {"Route_id":trip.Route_id,"route_name":trip.route_name,'route_origin':trip.route_origin,'route_destination':trip.route_destination,"route_stops":trip.route_stops},
#                     'driver_name': trip.driver_name,
#                     'booking_info': booking_info  # Include booking details if found
#                 })
#             return JsonResponse(data, safe=False)
#         else:
#             return JsonResponse({'error': 'Unable to fetch trips'}, status=response.status_code)


#     elif request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             booking_service_url=f'http://127.0.0.1:9000/api/booking-listings/{data["trip_id"]}/'
#             # route = Route.objects.get(Route_id=data['Route_id']) # "http://127.0.0.1:8000/route/route-listings/?Route_id=Route_id"
#             booking_response=requests.get(booking_service_url)
#             if booking_response.status_code == 200:
#                 trip = Trip.objects.create(
#                     trip_id=data['trip_id'],
#                     user_id=data['user_id'],
#                     vehicle_id=data['vehicle_id'],
#                     Route_id=data['Route_id'],  
#                     driver_name=data['driver_name'])
            
#             return JsonResponse({"id": trip.trip_id}, status=200)
#         except ValidationError as ve:
#             return JsonResponse({"errors": ve.messages}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
    
   
# @csrf_exempt
# def trip_detail(request, pk):
#     try:
#         trip = Trip.objects.get(trip_id=pk)
#     except Trip.DoesNotExist:
#         return JsonResponse({'error': 'Trip not found'}, status=404)
#     booking_service_url=f'http://127.0.0.1:9000/api/booking-details/{pk}/'

#     if request.method == "GET":
#         booking_response = requests.get(booking_service_url)

#         print(booking_response)
#         if booking_response.status_code == 200:

#             booking_info = booking_response.json()  # Get trip data

#             return JsonResponse({
#                     "trip_id": trip.trip_id,
#                     "user_id": trip.user_id,
#                     "vehicle_id": trip.vehicle_id,
#                     "Route_id":{"Route_id": trip.Route_id,"user_id":trip.Route_id.user_id,"route_name":trip.Route_id.route_name,"route_origin":trip.Route_id.route_origin,"route_destination":trip.Route_id.route_destination,"route_stops":trip.Route_id.route_stops},
#                     "driver_name": trip.driver_name,
#                     "booking_info" :booking_info},status=200)
#         else:
#             return JsonResponse({"error": "booking details not found"}, status=booking_response.status_code)
@csrf_exempt
# @UserAccessPermission
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
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            # trip = Trip.objects.create(**data)
            trip=Trip.objects.create( 
                trip_id=data['trip_id'],
                user_id=data['user_id'],
                vehicle_id=data['vehicle_id'],
                Route_id=data['Route_id'],
                driver_name=data['driver_name'])
                   
            trip.save()
            return JsonResponse({"id": trip.id}, status=201)
        except ValidationError as ve:
             return JsonResponse({"error": str(e)}, status=500)
   
      
        
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
   
    
       

   

    

