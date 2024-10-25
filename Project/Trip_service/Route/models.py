from django.db import models

def generate_route_id():
    last_route = Route.objects.all().order_by('Route_id').last()
    if not last_route:
        return 'RT00000001'
    last_id = int(last_route.Route_id[2:])
    new_id = last_id + 1
    return f'RT{str(new_id).zfill(8)}'

class Route(models.Model):
    Route_id = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=generate_route_id,
        editable=False
    )
    user_id = models.IntegerField(unique=True, null=True, blank=True)
    route_name = models.CharField(max_length=255)
    route_origin = models.CharField(max_length=255)
    route_destination = models.CharField(max_length=255)
    route_stops = models.JSONField(blank=True)

    def save(self, *args, **kwargs):
        if not self.Route_id:
            self.Route_id = generate_route_id()
        
        if not self.user_id:
            last_user = Route.objects.all().order_by('User_id').last()
            if not last_user:
                self.user_id = 1
            else:
                new_user_id = last_user.user_id + 1
                while Route.objects.filter(user_id=new_user_id).exists():
                    new_user_id += 1
                self.user_id = new_user_id
        
        super(Route, self).save(*args, **kwargs)

    def __str__(self):
        return self.Route_id
