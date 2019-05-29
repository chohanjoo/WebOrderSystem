from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('',views.drink_list, name='list'),
    path('request/add_menu',views.add_menu, name='add_menu'),
]
