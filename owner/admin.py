from django.contrib import admin
from .models import Shop,MenuBoard
# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['shopName']

@admin.register(MenuBoard)
class MenuBoardAdmin(admin.ModelAdmin):
    list_display = ['menuBoardID','shopID']