from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('<int:shopID>/<int:menuboardID>/index/',views.drink_list, name='list'),
    path('<int:shopID>/<int:menuboardID>/index/<int:categoryID>/',views.drink_list_category, name='list_category'),
    path('add/',views.add_menu, name='add_menu'),
    path('<int:shopID>/<int:menuboardID>/detail/<int:pk>/',views.menu_detail, name='menu_detail'),
    # path('add/menuboard',views.add_menuboard, name='add_menuboard'),
    # path('add/category', views.add_category, name='add_category'),
    # path('add/shop', views.add_shop, name='add_shop'),
]
