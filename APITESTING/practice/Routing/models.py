from django.db import models

# Create your models here.
from django.db import models
import re
from django.core.exceptions import ValidationError




def validate_Route_id(value):

    if not re.match(r'^RT\d{8}$', value):
      raise ValidationError('ID must start with "RT" and be followed by 8 digits')
    return value

def increment_Route_id():
      last_route = Routing.objects.all().order_by('Route_id').last()
      if not last_route:
          return 'RT00000001'
      route_id = last_route.Route_id
      route_int = int(route_id[2:10])
      new_route_int = route_int + 1
      new_route_id = 'RT' + str(new_route_int).zfill(8)
      return new_route_id 

def save(self, *args, **kwargs):
        if not self.Route_id:
            self.Route_id = increment_Route_id()
        super(Routing, self).save(*args, **kwargs)


class Routing(models.Model):
    Route_id=models.CharField(primary_key=True,max_length=10,unique=True,validators=[validate_Route_id])
    user_id=models.IntegerField(unique=True)
    # user_id = models.AutoField(unique=True)
    route_name=models.CharField(max_length=255)
    route_origin=models.CharField(max_length=255)
    route_destination=models.CharField(max_length=255)
    route_stops = models.JSONField(default=list, blank=True)


    def __str__(self):
        return self.Route_id
    
    def save(self, *args, **kwargs):
        if not self.Route_id:
            self.Route_id = increment_Route_id()
        super(Routing, self).save(*args, **kwargs)