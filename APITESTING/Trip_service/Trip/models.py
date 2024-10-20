from django.db import models
#from Trip_service.Route.models import Route
#from Route.models import Route_route
from  Route.models import Route
import re
from django.core.exceptions import ValidationError


def validate_trip_id(value):

    if not re.match(r'^TP\d{8}$', value):
      raise ValidationError('ID must start with "TP" and be followed by 8 digits')

# Create your models here.
class Trip(models.Model):
    trip_id=models.CharField(primary_key=True,max_length=10,validators=[validate_trip_id])
    user_id=models.IntegerField(unique=True)
    vehicle_id=models.IntegerField()
    Route_id=models.ForeignKey(Route, on_delete=models.CASCADE)
    driver_name=models.CharField(max_length=255)

    def __str__(self):
        return self.trip_id
    
    # def save(self,trip_id):
    #     if not self.trip_id.startswith('TP') or len(self.trip_id)!=10:
    #         raise ValueError("Trip id must be starts with 'TP' followed by 8 digits")
    #     super().save(trip_id)

    