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

    # def update(self, instance, validated_data):
    #     instance.trip_id = validated_data.get('trip_id', instance.trip_id)
    #     instance.traveller_name = validated_data.get('traveller_name', instance.traveller_name)
    #     instance.traveller_number = validated_data.get('traveller_number', instance.traveller_number)
    #     instance.ticket_cost = validated_data.get('ticket_cost', instance.ticket_cost)
    #     instance.traveller_email = validated_data.get('traveller_email', instance.traveller_email)
    #     instance.full_clean()
    #     instance.save()
    #     return instance
    