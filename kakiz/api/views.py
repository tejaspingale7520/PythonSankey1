from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def get_users(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(UserSerializer.data)

@api_view(['POST'])
def create_user(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT','DELETE'])
# def user_details(request,pk):
#     try:
#         user=User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method =='DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method =="PUT":
#         data=request.data
#         serializer=UserSerializer(User,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data
    serializer = UserSerializer(user, data=data)  # Pass the user instance for update
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])  ##for delete user
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




