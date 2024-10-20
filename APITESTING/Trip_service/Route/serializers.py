from rest_framework import serializers

#from django.core.validators import RegexValidator

class RouteSerializer(serializers.Serializer):
    Route_id = serializers.CharField()
    user_id=serializers.IntegerField()
    route_name=serializers.CharField(max_length=255)
    route_origin=serializers.CharField(max_length=255)
    route_destination=serializers.CharField(max_length=255)
    route_stops=serializers.CharField()
    


# def validate_Route_id(value):

#     if not re.match(r'^AT\d{8}$', value):
#       raise ValidationError('ID must start with "AT" and be followed by 8 digits')

    

