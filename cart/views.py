from django.shortcuts import render,redirect
from .cart import Cart
from menu.models import Menu
from .kakaopay import kakaopay_request, insert_success_url
from menu.models import Category

# Create your views here.

def cart_list(request,shopID,menuboardID):
    cart = Cart(request)
    total_price = 0
    category_list = Category.objects.all()
    for item in cart.cart.item_set.all():
        total_price = total_price + item.total_price
    return render(request,'cart/cart_list.html',{
        'cart' : cart,
        'total_price' : total_price,
        'category_list' : category_list,
        'shopID' : shopID,
        'menuboardID' : menuboardID,
    })


def add_to_cart(request,shopID,menuboardID, menu_id, quantity):
    menu = Menu.objects.get(id=menu_id)
    cart = Cart(request)
    cart.add(menu, menu.price, quantity)
    return redirect('cart:cart_list',shopID=shopID,menuboardID=menuboardID)

def remove_from_cart(request, product_id):
    menu = Menu.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(menu)

def get_cart(request):
    return render(request, 'cart_list.html', {'cart': Cart(request)})

def pay(request,shopID,menuboardID):   
    success_url = 'http://127.0.0.1:8000/orderingQueue/' + str(shopID) +'/'+ str(menuboardID) + '/'
    insert_success_url(success_url)
    url = kakaopay_request(request)
    return redirect(url)