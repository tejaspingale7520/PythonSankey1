from django.contrib import admin
from .models import Booking
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=['ticket_id','trip_id','traveller_name','traveller_number','ticket_cost','traveller_email']
