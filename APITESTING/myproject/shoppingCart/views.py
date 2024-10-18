from django.shortcuts import render
import json
from .models import CartItem
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import status


##validation 

def validate_cart_item(data):

        special_chars="!@#$%^&*()_+=,<>/"

        if any(c in special_chars
                for c in data['product_name']):
            raise ValidationError('product_name cannot contain special characters')

        if data.get('product_price') is not None and  data['product_price'] <=0:
            raise ValidationError('product_price must be a non zero')
        
        if data.get('product_quantity') is not None and data['product_quantity']==0:
            raise ValidationError('Please add at least 1 product ')
        
        return data


# Create your views here.
def create_cart(request):
    try:
      data = json.loads(request.body)
      validate_cart_item(data)

      cart_Item = CartItem.objects.create( product_name = data['product_name'],
                                product_price = data['product_price'], 
                                product_quantity = data['product_quantity'])
    
    
      return JsonResponse({'new iten added to cart with id': cart_Item.id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

  

def get_cart_details(request):
    try:

     items=CartItem.objects.all()
    #  items_data=[]
    #  for item in items:
    #     data={'id':item.id,'product_name':item.product_name,'product_price':item.product_price,'product_quantity':item.product_quantity}
    #     items_data.append(data)
     items_data=[ item for item in items]
     return JsonResponse(items_data,safe=False)
    except CartItem.DoesNotExist:
        return JsonResponse({'msg':'no data found'}, status=404)

    

   # by id to get parameter
def get_item(request,pk):
    try:
        item= CartItem.objects.get(id=pk)
        data = {"id": item.id, 
                "product_name": item.product_name, 
                "product_price": item.product_price,
                  "product_quantity": item.product_quantity}
        return JsonResponse(data)
    except item.DoesNotExist:
        return JsonResponse({"error": "item not found"}, status=404)
    

def update_item(request, pk):
    try:
        item= CartItem.objects.get(id=pk)
        data = json.loads(request.body)
        validate_cart_item(data)

        item.product_name = data.get('product_name', item.product_name)
        item.product_price = data.get('product_price', item.product_price)
        item.product_quantity = data.get('product_quantity', item.product_quantity)
        item.save()
        return JsonResponse({' cart successfully wpdated with id': item.id })

    except CartItem.DoesNotExist:
        return JsonResponse({"error": "item not found"}, status=404)
    

def update_itempartial(request, pk):
    try:
        item= CartItem.objects.get(id=pk)
        data = json.loads(request.body)
        validate_cart_item(data)
        item.product_name = data.get('product_name', item.product_name)
        item.product_price = data.get('product_price', item.product_price)
        item.product_quantity = data.get('product_quantity', item.product_quantity)
        
        item.save()

        return JsonResponse({'cart updated with id': item.id})

    except CartItem.DoesNotExist:
        return JsonResponse({"error": "item not found"}, status=404)
    
    
    

#to delete particular item
def delete_item(request, pk):
    try:
        item = CartItem.objects.get(id=pk)
        item.delete()
        return JsonResponse({'message': 'item is deleted'}, status=204)
    except CartItem.DoesNotExist:
        return JsonResponse({"error": "item not found"}, status=404)
    

def search_item(request):
    
    query = request.GET.get('query', '')
    items = CartItem.objects.filter(product_name__icontains=query) | CartItem.objects.filter(product_name__startswith=query) | CartItem.objects.filter(product_price__icontains=query)   ## you can serach with name
    #items=CartItem.objects.filter(product_name__startswith=query).values()    ##you can seacrch with start letter
    #items=CartItem.objects.filter(product_name='product_name').values() 
    
    
    item_info = []
    for item in items:
        data = {
            'product_name': item.product_name,
            'product_price':item.product_price,
            'product_quantity': item.product_quantity
        }
        item_info.append(data)
    return JsonResponse(item_info,safe=False)

def search_itemsorder(request):
    query=request.GET.get('order_by','-product_price')
    
    if query not in ['product_price', 'product_quantity']:
        return JsonResponse({'error': 'Invalid query parameter'}, status=400)
    items = CartItem.objects.all().order_by(query).values()
    
    # item_info=[]
    # for item in items:
    #     data = {
    #         'product_name': item['product_name'],
    #         'product_price':item['product_price'],
    #         'product_quantity': item['product_quantity']
    #     }
    #     item_info.append(data)
    item_info=[ item for item in items]
    return JsonResponse(item_info,safe=False)


    
    
    
    
    



    