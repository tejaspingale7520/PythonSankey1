from rest_framework import serializers
from .models import Booking
from django.core.validators import RegexValidator

class BookingSerializer(serializers.Serializer):
    ticket_id = serializers.CharField(max_length=10, read_only=True)
    trip_id = serializers.CharField(max_length=10)
    traveller_name = serializers.CharField(max_length=255)
    traveller_number = serializers.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='Traveller number must be 10 digits')]
    )
    ticket_cost = serializers.FloatField()
    traveller_email = serializers.EmailField()

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)

    
    