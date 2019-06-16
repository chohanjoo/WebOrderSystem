from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('<int:shopID>/<int:menuboardID>/list/',views.cart_list, name='cart_list'),
    path('<int:shopID>/<int:menuboardID>/add/<int:menu_id>/<int:quantity>/', views.add_to_cart, name='cart_add'),
    path('<int:shopID>/<int:menuboardID>/pay/',views.pay, name='pay'),
    
]
