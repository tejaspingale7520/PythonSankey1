from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.db.models import Q
from .models import Booking
from .serializers import BookingSerializer
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.exceptions import ValidationError


# class BookingPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# @csrf_exempt
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def booking_listing(request):
#     if request.method == 'GET':
#         bookings = Booking.objects.all()

#         # Implementing search functionality
#         search_query = request.GET.get('search', None)
#         print(search_query)
#         if search_query:
#             bookings = bookings.filter(
#                 trip_id=search_query
#             )
#         else:
#             return Response({'error': 'search query is needed'})
#         # Implementing sort functionality
#         sort_by = request.GET.get('sort_by', None)
#         if sort_by in ['ticket_id', 'traveller_name', 'trip_id']:
#             bookings = bookings.order_by(sort_by)

        # paginator = PageNumberPagination()      #according to page number nexr>> previous<<<
        # paginator.page_size=5
        # paginated_data=paginator.paginate_queryset(bookings,request)
        # print(paginated_data)
        # paginator=LimitOffsetPagination()  #to set limit from 100 and page size 5 get data from 100-105 in 1st page
        # paginator.page_size=5
        # paginated_data=paginator.paginate_queryset(bookings,request)

        # paginator=CursorPagination()    #it has functionality to order by particular field 
        # paginator.page_size=10
        # paginator.ordering='traveller_name'
        # paginated_data=paginator.paginate_queryset(bookings,request)


       
        # serializer = BookingSerializer(bookings, many=True)

        # return Response({"data":serializer.data})
        # return paginator.get_paginated_response(serializer.data)
        # return Responsse()

    # elif request.method == 'POST':
    #     serializer = BookingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         booking = Booking(
    #         ticket_id=serializer.validated_data['ticket_id'],
    #         trip_id=serializer.validated_data['trip_id'],
    #         traveller_name=serializer.validated_data['traveller_name'],
    #         traveller_number=serializer.validated_data['traveller_number'],
    #         ticket_cost=serializer.validated_data['ticket_cost'],
    #         traveller_email=serializer.validated_data['traveller_email'],
    #         )
    #         booking.save()
    #         return Response({"message": "Booking created", "ticket_id": booking.ticket_id}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# import requests
# from requests.auth import HTTPBasicAuth
# import json

# url = 'http://127.0.0.1:8000/api/booking-listings/'
# username = 'your_username'
# password = 'your_password'
# data = {
#     'trip_id': 'TP00000001',
#     'ticket_id': 'TK00000001',
#     'traveller_name': 'John Doe',
#     'traveller_number': '1234567890',
#     'ticket_cost': 100.50,
#     'traveller_email': 'johndoe@example.com'
# }

# response = requests.post(url, auth=HTTPBasicAuth(username, password), data=json.dumps(data), headers={'Content-Type': 'application/json'})

# if response.status_code == 201:
#     print(response.json())
# else:
#     print(f"Error: {response.status_code}")



@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def booking_listing(request):
    if request.method == "GET":
        # Fetch trips from the TripService
        trip_service_url = 'http://127.0.0.1:8000/trip/trip-listings/' 
       
        response = requests.get(trip_service_url)
        if response.status_code == 200:
            trips = response.json()  # Get trip data
            
            # Prepare booking data along with trip information
            bookings = Booking.objects.all()

              # Implementing search functionality
            search_query = request.GET.get('search', None)
            #   print(search_query)
            if search_query:
                bookings = bookings.filter(
                    trip_id=search_query
                )  

            # Implementing sort functionality
            sort_by = request.GET.get('sort_by', None)

            if sort_by in ['ticket_id', 'traveller_name', 'trip_id']:
                bookings = bookings.order_by(sort_by)
            # else:
            #     return Response({'error': 'query input is needed'})

            paginator = PageNumberPagination()      #according to page number nexr>> previous<<<
            paginator.page_size=5
            paginated_data=paginator.paginate_queryset(bookings,request)
            data = []
            for booking in paginated_data:
                trip_info = next((trip for trip in trips if trip['trip_id'] == booking.trip_id), None)
                data.append({
                    'ticket_id': booking.ticket_id,
                    'trip_id': booking.trip_id,
                    'traveller_name': booking.traveller_name,
                    'traveller_number': booking.traveller_number,
                    'ticket_cost': booking.ticket_cost,
                    'traveller_email': booking.traveller_email,
                    'trip_info': trip_info  # Include trip details if found
                })
            # return Response(data, status=status.HTTP_200_OK)
            return paginator.get_paginated_response(data)
        else:
            return Response({'error': 'Unable to fetch trips'}, status=response.status_code)

    elif request.method == 'POST':
        data = json.loads(request.body)
        # Fetch trip details from TripService
        trip_service_url = f'http://localhost:8000/trip/trip-details/{data['trip_id']}/'
       
        trip_response = requests.get(trip_service_url)
        if trip_response.status_code == 200:
            # Trip exists, proceed with booking
            serializer = BookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Trip not found"}, status=status.HTTP_404_NOT_FOUND)
        

@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def booking_detail(request, pk):
    try:
        booking = Booking.objects.get(ticket_id=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
    
    trip_service_url = f'http://localhost:8000/trip/trip-details/{booking.trip_id}/' 

    if request.method == "GET":
        # Fetch trip details from TripService
        trip_response = requests.get(trip_service_url)
        if trip_response.status_code == 200:
            trip_info = trip_response.json()  # Get trip data
            return Response({
                "ticket_id": booking.ticket_id,
                "trip_id": booking.trip_id,
                "traveller_name": booking.traveller_name,
                "traveller_number": booking.traveller_number,
                "ticket_cost": booking.ticket_cost,
                "traveller_email": booking.traveller_email,
                "trip_info": trip_info  # Include trip details
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Trip details not found"}, status=trip_response.status_code)

    elif request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(booking, key, value)
            booking.full_clean()
            booking.save()
            return Response({"message": "Booking updated"}, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({"errors": ve.messages}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == "DELETE":
        booking.delete()
        return Response({'message': "Booking deleted"}, status=status.HTTP_200_OK)



# @csrf_exempt
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def booking_detail(request, pk):
#     try:
#         booking = Booking.objects.get(trip_id=pk)
#     except Booking.DoesNotExist:
#         return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BookingSerializer(booking)
#         #return Response(serializer.data)
#         return Response({"ticket_id": booking.ticket_id, "trip_id": booking.trip_id, "traveller_name": booking.traveller_name, "traveller_number": booking.traveller_number,"ticket_cost":booking.ticket_cost,"traveller_email":booking.traveller_email})

#     elif request.method in ['PUT', 'PATCH']:
#         serializer = BookingSerializer(booking, data=request.data, partial=True)

#         if serializer.is_valid():
             
#             booking.ticket_id=serializer.validated_data.get('ticket_id',booking.ticket_id)
#             booking.trip_id = serializer.validated_data.get('trip_id', booking.trip_id)
#             booking.traveller_name = serializer.validated_data.get('traveller_name', booking.traveller_name)
#             booking.traveller_number = serializer.validated_data.get('traveller_number', booking.traveller_number)
#             booking.ticket_cost=serializer.validated_data.get('ticket_cost',booking.ticket_cost)
#             booking.traveller_email=serializer.validated_data.get('traveller_email',booking.traveller_email)
#             booking.save()
#             #booking = serializer.save()
#             return Response({"message": "Booking updated"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         booking.delete()
#         return Response({'message': "Booking deleted"}, status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def booking_detail(request, pk):
#     try:
#         booking = Booking.objects.get(ticket_id=pk)
#     except Booking.DoesNotExist:
#         return JsonResponse({'error': 'Booking not found'}, status=404)

#     trip_service_url = f'http://localhost:8000/trip/trip-details/{booking.trip.trip_id}/'  # Adjust according to your service URL

#     if request.method == "GET":
#         # Fetch trip details from TripService
#         trip_response = requests.get(trip_service_url)

#         if trip_response.status_code == 200:
#             trip_info = trip_response.json()  # Get trip data

#             return JsonResponse({
#                 "ticket_id": booking.ticket_id,
#                 "trip_id": booking.trip.trip_id,
#                 "traveller_name": booking.traveller_name,
#                 "traveller_number": booking.traveller_number,
#                 "ticket_cost": booking.ticket_cost,
#                 "traveller_email": booking.traveller_email,
#                 "trip_info": trip_info  # Include trip details
#             })
#         else:
#             return JsonResponse({"error": "Trip details not found"}, status=trip_response.status_code)

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
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
# from rest_framework import status
# from .models import Booking
# from .serializers import BookingSerializer
# import requests
# import json

# @api_view(['GET', 'POST'])
# def booking_listing(request):
#     if request.method == "GET":
#         # Fetch trips from the TripService
#         trip_service_url = 'http://127.0.0.1:8000/trip/trip-listings/'  # Adjust according to your service URL
#         response = requests.get(trip_service_url)
#         if response.status_code == 200:
#             trips = response.json()  # Get trip data
            
#             # Prepare booking data along with trip information
#             bookings = Booking.objects.all()

#             # Implementing search functionality
#             search_query = request.GET.get('search', None)
#             if search_query:
#                 bookings = bookings.filter(trip_id=search_query)

#             # Implementing sort functionality
#             sort_by = request.GET.get('sort_by', None)
#             if sort_by in ['ticket_id', 'traveller_name', 'trip_id']:
#                 bookings = bookings.order_by(sort_by)

#             # Implement pagination
#             paginator = PageNumberPagination()
#             paginator.page_size = 5
#             paginated_data = paginator.paginate_queryset(bookings, request)

#             data = []
#             for booking in paginated_data:
#                 trip_info = next((trip for trip in trips if trip['trip_id'] == booking.trip_id), None)
#                 data.append({
#                     'ticket_id': booking.ticket_id,
#                     'trip_id': booking.trip_id,
#                     'traveller_name': booking.traveller_name,
#                     'traveller_number': booking.traveller_number,
#                     'ticket_cost': booking.ticket_cost,
#                     'traveller_email': booking.traveller_email,
#                     'trip_info': trip_info  # Include trip details if found
#                 })

#             return paginator.get_paginated_response(data)
#         else:
#             return Response({'error': 'Unable to fetch trips'}, status=response.status_code)

#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         # Fetch trip details from TripService
#         trip_service_url = f'http://localhost:8000/trip/trip-details/{data["trip_id"]}/'
#         trip_response = requests.get(trip_service_url)
#         if trip_response.status_code == 200:
#             # Trip exists, proceed with booking
#             serializer = BookingSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "Trip not found"}, status=status.HTTP_404_NOT_FOUND)
