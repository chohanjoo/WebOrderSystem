from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('',views.drink_list, name='list'),
    path('add/menu',views.add_menu, name='add_menu'),
    # path('add/menuboard',views.add_menuboard, name='add_menuboard'),
    # path('add/category', views.add_category, name='add_category'),
    # path('add/shop', views.add_shop, name='add_shop'),
]
