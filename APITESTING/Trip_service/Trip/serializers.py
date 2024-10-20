from rest_framework import serializers
from django.core.validators import RegexValidator
from Route.models import Route
from .models import Trip



class TripSerializer(serializers.Serializer):

    trip_id = serializers.CharField()
    user_id=serializers.IntegerField()
    vehicle_id=serializers.IntegerField()
    #Route_id=serializers.ForeignKey(Route,related_name='routes', on_delete=serializers.CASCADE)
    Route_id = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all())
    driver_name=serializers.CharField(max_length=255)
    


    # def validate_trip_id(value):
    #     if not re.match('TP\d{8}$',value):
    #         raise serializers.ValidationError("Trip_id must start with 'TP' and follwed by 8 digits")
    #     return value
    

