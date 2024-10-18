from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer,LoginSerializer,RegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework .authentication import TokenAuthentication,BasicAuthentication



class RegisterAPI(APIView):
    def post(self,request):
        data=request.data 
        serializer=RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':False,'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response({'status':True,'message':'user created'},status=status.HTTP_201_CREATED)
    
class LoginAPI(APIView):
    def post(self,request):
        data=request.data
        serializer =LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':False,'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
        user=authenticate(username=serializer.data['username'],
                      password=serializer.data['password'])
        if not user:
            return Response({'status':False,'msg':'invalid credential'},status=status.HTTP_400_BAD_REQUEST)
        

        token,_ = Token.objects.create(user=user)
        # return Response({'status':True,'message':'user login','token':str(token)},status=status.HTTP_201_CREATED)
        return Response({'status':True,'msg':'login successfully'},status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    data=request.data
    serializer=LoginSerializer(data=data)
    if serializer.is_valid():
        data=serializer.validated_data
        #print(serializer.data)
        return Response({'msg':'created succeefully'})
    else:

        return Response(serializer.errors)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_list(request):

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def item_create(request):

    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        item = Item(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            price=serializer.validated_data['price'],
           
        )
        item.save()
        return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ItemSerializer(item)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def item_update(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        item.name = serializer.validated_data.get('name', item.name)
        item.description = serializer.validated_data.get('description', item.description)
        item.price = serializer.validated_data.get('price', item.price)
        item.save()
        return Response(ItemSerializer(item).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
#@permission_classes([IsAuthenticated])
def item_partialupdate(request, pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        item.name = serializer.validated_data.get('name', item.name)
        item.description = serializer.validated_data.get('description', item.description)
        item.price = serializer.validated_data.get('price', item.price)
        item.save()
        return Response(ItemSerializer(item).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def item_delete(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({'msg:'f'the details with id:{pk} not found'},status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({'msg:'f'data deleted for id:{pk}'},status=status.HTTP_204_NO_CONTENT)