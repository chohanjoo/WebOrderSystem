from django.shortcuts import render,redirect
from .cart import Cart
from menu.models import Menu

# Create your views here.

def cart_list(request):
    cart = Cart(request)
    return render(request,'cart/cart_list.html',{
        'cart' : cart,
    })


def add_to_cart(request, menu_id, quantity):
    menu = Menu.objects.get(id=menu_id)
    cart = Cart(request)
    cart.add(menu, menu.price, quantity)
    return redirect('cart:cart_list')

def remove_from_cart(request, product_id):
    menu = Menu.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(menu)

def get_cart(request):
    return render(request, 'cart_list.html', {'cart': Cart(request)})