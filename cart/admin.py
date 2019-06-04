from django.contrib import admin
from .models import Cart,Item
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['creation_date']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['cart','object_id','quantity','unit_price']