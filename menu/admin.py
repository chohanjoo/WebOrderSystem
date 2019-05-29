from django.contrib import admin
from .models import Shop,MenuBoard,Category,Menu
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['shopName']

@admin.register(MenuBoard)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menuBoardID','shopID']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price' ,'image']
