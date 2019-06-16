from django.shortcuts import render,redirect
import random
# Create your views here.
order_list = []

def order_add(request):
    order_number = random.randrange(1,10000)
    order_list.append(order_number)
    return render(request,'orderingQueue/order_add.html',{
        'order_number' : order_number,
    })

def order_delete(request,order_number):
    order_list.remove(order_number)
    return render(request,'orderingQueue/order_list.html',{
        'order_list' : order_list,
    })

def order_queue(request,shopID,menuboardID):
    return render(request,'orderingQueue/order_list.html',{
        'order_list' : order_list,
    })
