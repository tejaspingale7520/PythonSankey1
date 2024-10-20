from django.db import models
import re,random
from django.core.exceptions import ValidationError


def validate_Route_id(value):

    if not re.match(r'^RT\d{8}$', value):
      raise ValidationError('ID must start with "RT" and be followed by 8 digits')

def generate_unique_id(self):
    while True:
        unique_id="RT" + str(random.randint(0,99999999)).zfill(8)
        if not Route.objects.filter(route_id=unique_id).exists():
            return unique_id
# Create your models here.

class Route(models.Model):
    Route_id=models.CharField(primary_key=True,max_length=10,unique=True,validators=[validate_Route_id])
    user_id=models.IntegerField(unique=True)
    route_name=models.CharField(max_length=255)
    route_origin=models.CharField(max_length=255)
    route_destination=models.CharField(max_length=255)
    route_stops = models.JSONField(default=list, blank=True)


    def __str__(self):
        return self.route_name  
    


