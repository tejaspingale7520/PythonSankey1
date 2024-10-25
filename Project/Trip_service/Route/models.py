from django.db import models
from django.utils.crypto import get_random_string

def generate_id(prefix):
    random_part = get_random_string(8, allowed_chars='0123456789')
    return f"{prefix}{random_part}"

class Route(models.Model):
    Route_id = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=generate_id('RT')
    )
    user_id = models.IntegerField(unique=True, null=True, blank=True)  # Manually handled
    route_name = models.CharField(max_length=255)
    route_origin = models.CharField(max_length=255)
    route_destination = models.CharField(max_length=255)
    route_stops = models.JSONField(blank=True)

    def save(self, *args, **kwargs):
        if not self.Route_id:
            self.Route_id = generate_id('RT')
        if not self.user_id:
            last_user = Route.objects.all().order_by('id').last()
            if not last_user:
                self.user_id = 1
            else:
                self.user_id = last_user.user_id + 1
        super(Route, self).save(*args, **kwargs)

    def __str__(self):
        return self.Route_id
