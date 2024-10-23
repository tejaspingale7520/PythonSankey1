# import os
# import django
# from faker import Faker
# import random
 
 
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trip_service.settings')  
# django.setup()
 
# from Trip.models import Trip 
# from Route.models import Route
 
# fake = Faker()
 
# def create_dummy_trips(num=10):
#     routes = Route.objects.all()  # Get all existing routes
#     for _ in range(num):
#         trip_id = f'TP{fake.random_int(min=10000000, max=99999999)}'
#         trip = Trip(
#             trip_id=trip_id,
#             user_id=fake.random_int(min=101, max=200),
#             vehicle_id=fake.random_int(min=1, max=5000),  # Assuming vehicle_id is a number
#             Route_id=random.choice(routes) if routes else None,  # Randomly assign an existing route
#             driver_name=fake.name()
#         )
#         trip.save()
#         print(f'Created trip: {trip}')
 
# if __name__ == "__main__": 
#     create_dummy_trips(50)  

import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trip_service.settings')  
django.setup()

from Trip.models import Trip 
from Route.models import Route 

fake = Faker()

def create_dummy_trips(num=10):
    routes = Route.objects.all()  # Get all existing routes
    for _ in range(num):
        trip_id = f'TP{fake.random_int(min=10000000, max=99999999)}'
        if routes:
            route = random.choice(routes)  # Randomly assign an existing route
        else:
            continue  # Skip if there are no routes

        Trip.objects.create(
            trip_id=trip_id,
            user_id=fake.random_int(min=1, max=50),  # Ensure this user exists
            vehicle_id=fake.random_int(min=1, max=5000),  # Assuming vehicle_id is a number
            Route_id=route,  # Properly set the foreign key
            driver_name=fake.name()
        )

if __name__ == "__main__": 
    create_dummy_trips(50)
