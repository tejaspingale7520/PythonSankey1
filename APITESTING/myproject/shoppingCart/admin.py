from django.contrib import admin
from .models import CartItem

# Register your models here.
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_price','product_quantity']
    
