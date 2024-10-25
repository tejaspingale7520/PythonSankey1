from django.db import models
from Route.models import Route

def generate_trip_id():
    last_trip = Trip.objects.all().order_by('trip_id').last()
    if not last_trip:
        return 'TP00000001'
    last_id = int(last_trip.trip_id[2:])
    new_id = last_id + 1
    return f'TP{str(new_id).zfill(8)}'

class Trip(models.Model):
    trip_id = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=generate_trip_id,
        editable=False
    )
    user_id = models.IntegerField(unique=True, null=True, blank=True)
    vehicle_id = models.IntegerField(unique=True)
    Route_id = models.ForeignKey(Route, on_delete=models.CASCADE, to_field='Route_id')
    driver_name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.trip_id:
            self.trip_id = generate_trip_id()
        
        if not self.user_id:
            last_user = Trip.objects.all().order_by('user_id').last()
            if not last_user:
                self.user_id = 1
            else:
                new_user_id = last_user.user_id + 1
                while Trip.objects.filter(user_id=new_user_id).exists():
                    new_user_id += 1
                self.user_id = new_user_id
        
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return self.driver_name
