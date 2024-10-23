# import os
# import django
# from faker import Faker
# import random
 
 
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trip_service.settings')  
# django.setup()
 
# from Trip.models import Trip 
# from Route.models import Route
 
# fake = Faker()
 
# def create_dummy_routes(num=10):
#     for _ in range(num):
#         Route_id = f'RT{fake.random_int(min=10000000, max=99999999)}'
#         route_origin = fake.city()
#         route_destination = fake.city()
#         route_name = f'{route_origin} - {route_destination}'
#         route_stops = [{'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name':fake.city()} for _ in range(random.randint(1, 5))]  # Random number of stops
#         route_stops.insert(0, {'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name': route_origin})
#         route_stops.append({'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name':route_destination})
#         route = Route(
#             Route_id=Route_id,
#             user_id=fake.random_int(min=1, max=100),
#             route_name=route_name,
#             route_origin=route_origin,
#             route_destination=route_destination,
#             route_stops=route_stops
#         )
#         route.save()
#         print(f'Created route: {route}')
 
# # def create_dummy_trips(num=10):
# #     routes = Route.objects.all()  # Get all existing routes
# #     for _ in range(num):
# #         trip_id = f'TP{fake.random_int(min=10000000, max=99999999)}'
# #         trip = Trip(
# #             trip_id=trip_id,
# #             user_id=fake.random_int(min=1, max=50),
# #             vehicle_id=fake.random_int(min=1, max=5000),  # Assuming vehicle_id is a number
# #             route=random.choice(routes) if routes else None,  # Randomly assign an existing route
# #             driver_name=fake.name()
# #         )
# #         trip.save()
# #         print(f'Created trip: {trip}')
 
# if __name__ == "__main__":
#     create_dummy_routes(50)  
#     #create_dummy_trips(50)  
import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trip_service.settings')  
django.setup()

from Route.models import Route

fake = Faker()

def create_dummy_routes(num=10):
    for _ in range(num):
        Route_id = f'RT{fake.random_int(min=10000000, max=99999999)}'
        route_origin = fake.city()
        route_destination = fake.city()
        route_name = f'{route_origin} - {route_destination}'
        route_stops = [
            {
                'lat': round(random.uniform(50, 500), 2), 
                'long': round(random.uniform(50, 500), 2), 
                'stop_name': fake.city()
            } for _ in range(random.randint(1, 5))
        ]
        route_stops.insert(0, {'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name': route_origin})
        route_stops.append({'lat': round(random.uniform(50, 500), 2), 'long': round(random.uniform(50, 500), 2), 'stop_name': route_destination})

        Route.objects.create(
            Route_id=Route_id,
            user_id=fake.random_int(min=1, max=100),  # Ensure this user exists
            route_name=route_name,
            route_origin=route_origin,
            route_destination=route_destination,
            route_stops=route_stops
        )

if __name__ == "__main__":
    create_dummy_routes(50)
