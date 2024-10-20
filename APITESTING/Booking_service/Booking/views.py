from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import json
from .models import Booking
from Trip.models import Trip
import requests
# @csrf_exempt
# def booking_listing(request):
#     if request.method == "GET":
#         bookings = Booking.objects.all()
#         data = [{'ticket_id': booking.ticket_id, 'trip_id': booking.trip.trip_id, 
#                  'traveller_name': booking.traveller_name, 'traveller_number': booking.traveller_number,
#                  'ticket_cost': booking.ticket_cost, 'traveller_email': booking.traveller_email} 
#                 for booking in bookings]
#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             trip = Trip.objects.get(trip_id=data['trip_id'])
#             booking = Booking(trip=trip, **data)
#             booking.full_clean()
#             booking.save()
#             return JsonResponse({"message": "Booking created", "ticket_id": booking.ticket_id}, status=201)
#         except ValidationError as ve:
#             return JsonResponse({"errors": ve.messages}, status=400)
#         except Trip.DoesNotExist:
#             return JsonResponse({"error": "Trip not found"}, status=404)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def booking_listing(request):
    if request.method == "GET":
        # Fetch trips from the TripService
        trip_service_url = 'http://localhost:8000/trips/'  # Adjust according to your service URL
        response = requests.get(trip_service_url)

        if response.status_code == 200:
            trips = response.json()  # Get trip data
            
            # Prepare booking data along with trip information
            bookings = Booking.objects.all()
            data = []
            for booking in bookings:
                trip_info = next((trip for trip in trips if trip['trip_id'] == booking.trip.trip_id), None)
                data.append({
                    'ticket_id': booking.ticket_id,
                    'trip_id': booking.trip.trip_id,
                    'traveller_name': booking.traveller_name,
                    'traveller_number': booking.traveller_number,
                    'ticket_cost': booking.ticket_cost,
                    'traveller_email': booking.traveller_email,
                    'trip_info': trip_info  # Include trip details if found
                })
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'Unable to fetch trips'}, status=response.status_code)



    if request.method == 'POST':
        data = json.loads(request.body)
        # Fetch trip details from TripService
        trip_service_url = f'http://localhost:8000/trips/{data["trip_id"]}/'
        trip_response = requests.get(trip_service_url)

        if trip_response.status_code == 200:
            # Trip exists, proceed with booking
            booking = Booking.objects.create(
                ticket_id=data['ticket_id'],
                trip_id=data['trip_id'],
                traveller_name=data['traveller_name'],
                traveller_number=data['traveller_number'],
                ticket_cost=data['ticket_cost'],
                traveller_email=data['traveller_email'],
            )
            return JsonResponse({"id": booking.ticket_id}, status=201)
        else:
            return JsonResponse({"error": "Trip not found"}, status=404)
        

# @csrf_exempt
# def booking_detail(request, pk):
#     try:
#         booking = Booking.objects.get(ticket_id=pk)
#     except Booking.DoesNotExist:
#         return JsonResponse({'error': 'Booking not found'}, status=404)

#     if request.method == "GET":
#         return JsonResponse({
#             "ticket_id": booking.ticket_id,
#             "trip_id": booking.trip.trip_id,
#             "traveller_name": booking.traveller_name,
#             "traveller_number": booking.traveller_number,
#             "ticket_cost": booking.ticket_cost,
#             "traveller_email": booking.traveller_email
#         })

#     elif request.method in ['PUT', 'PATCH']:
#         try:
#             data = json.loads(request.body)
#             for key, value in data.items():
#                 setattr(booking, key, value)
#             booking.full_clean()
#             booking.save()
#             return JsonResponse({"message": "Booking updated"}, status=200)
#         except ValidationError as ve:
#             return JsonResponse({"errors": ve.messages}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     elif request.method == "DELETE":
#         booking.delete()
#         return JsonResponse({'message': "Booking deleted"}, status=200)

@csrf_exempt
def booking_detail(request, pk):
    try:
        booking = Booking.objects.get(ticket_id=pk)
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)

    trip_service_url = f'http://localhost:8000/trips/{booking.trip.trip_id}/'  # Adjust according to your service URL

    if request.method == "GET":
        # Fetch trip details from TripService
        trip_response = requests.get(trip_service_url)

        if trip_response.status_code == 200:
            trip_info = trip_response.json()  # Get trip data

            return JsonResponse({
                "ticket_id": booking.ticket_id,
                "trip_id": booking.trip.trip_id,
                "traveller_name": booking.traveller_name,
                "traveller_number": booking.traveller_number,
                "ticket_cost": booking.ticket_cost,
                "traveller_email": booking.traveller_email,
                "trip_info": trip_info  # Include trip details
            })
        else:
            return JsonResponse({"error": "Trip details not found"}, status=trip_response.status_code)

    elif request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(booking, key, value)
            booking.full_clean()
            booking.save()
            return JsonResponse({"message": "Booking updated"}, status=200)
        except ValidationError as ve:
            return JsonResponse({"errors": ve.messages}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "DELETE":
        booking.delete()
        return JsonResponse({'message': "Booking deleted"}, status=200)


