from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.Serializer):
    ticket_id = serializers.CharField(max_length=10)
    trip_id = serializers.CharField(max_length=10)
    traveller_name = serializers.CharField(max_length=255)
    traveller_number = serializers.CharField(max_length=10)
    ticket_cost = serializers.FloatField()
    traveller_email = serializers.EmailField()

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    
    