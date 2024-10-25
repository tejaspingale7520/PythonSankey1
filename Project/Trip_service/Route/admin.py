from django.contrib import admin
from .models import Route

# Register your models here.
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display=['Route_id','user_id','route_name','route_origin','route_destination','route_stops']