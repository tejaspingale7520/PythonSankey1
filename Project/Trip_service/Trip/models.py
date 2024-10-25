from django.db import models
from django.utils.crypto import get_random_string
from Route.models import Route

def generate_id(prefix):
    random_part = get_random_string(8, allowed_chars='0123456789')
    return f"{prefix}{random_part}"

class Trip(models.Model):
    trip_id = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=generate_id('TP')
    )
    user_id = models.IntegerField(unique=True, null=True, blank=True)  # Manually handled
    vehicle_id = models.IntegerField()
    Route_id= models.ForeignKey(Route, on_delete=models.CASCADE, to_field='Route_id')
    driver_name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.trip_id:
            self.trip_id = generate_id('TP')
        if not self.user_id:
            last_user = Trip.objects.all().order_by('id').last()
            if not last_user:
                self.user_id = 1
            else:
                self.user_id = last_user.user_id + 1
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return self.driver_name
