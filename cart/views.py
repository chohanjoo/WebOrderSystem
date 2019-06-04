from django.shortcuts import render,redirect
from .cart import Cart
from menu.models import Menu
from .kakaopay import kakaopay_request

# Create your views here.

def cart_list(request):
    cart = Cart(request)
    total_price = 0
    for item in cart.cart.item_set.all():
        total_price = total_price + item.total_price
    return render(request,'cart/cart_list.html',{
        'cart' : cart,
        'total_price' : total_price,
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

def pay(request):
    url = kakaopay_request(request)
    return redirect(url)