from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_list, name='cart_list'),
    path('add/<int:menu_id>/<int:quantity>/', views.add_to_cart, name='cart_add'),
    path('pay/',views.pay, name='pay'),
    
]
