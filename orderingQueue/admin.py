from django.contrib import admin
from .models import OrderNumber
# Register your models here.
@admin.register(OrderNumber)
class OrderNumberAdmin(admin.ModelAdmin):
    list_display = ['orderNumber']