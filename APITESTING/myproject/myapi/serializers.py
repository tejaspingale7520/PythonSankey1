from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User




class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self,data):

        if data['username']:
          if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username already taken')
          
        if data['email']:
          if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('email already taken')
          
        return data
    
    def create(self,validated_data):
       user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
       user.set_password(validated_data['password'])
       user.save()
       return validated_data





class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()




class ItemSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=10,decimal_places=2)

    def validate(self,data):

        special_chars="!@#$%^&*()_+=,<>/"
        if any(c in special_chars
                for c in data['name']):
            raise serializers.ValidationError('name cannot contain special characters')



        if data.get('price') is not None and data['price'] > 0:
            raise serializers.ValidationError('Price must be a positive number')
        return data
        
        
    
   
