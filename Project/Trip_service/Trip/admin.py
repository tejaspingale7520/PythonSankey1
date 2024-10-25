from django.contrib import admin
from .models import Trip

# Register your models here.
@admin.register(Trip)
class RouteAdmin(admin.ModelAdmin):
    list_display=['trip_id','user_id','vehicle_id','Route_id','driver_name']