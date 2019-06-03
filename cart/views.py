from django.shortcuts import render
from .cart import Cart
from menu.models import Menu

# Create your views here.

def cart_list(request):
    return render(request,'basket/cart_list.html')


def add_to_cart(request, product_id, quantity):
    menu = Menu.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(menu, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    menu = Menu.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(menu)

def get_cart(request):
    return render(request, 'cart_list.html', {'cart': Cart(request)})