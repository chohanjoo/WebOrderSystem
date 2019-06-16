from django.shortcuts import render,redirect
import random
from owner.models import MenuBoard
from .models import OrderNumber
# Create your views here.


def order_add(request,shopID,menuboardID):
    menuboard = MenuBoard.objects.get(menuBoardID=menuboardID)
    order_number = random.randrange(1,10000)
    OrderNumber(menuBoard=menuboard,orderNumber=order_number).save()
    return render(request,'orderingQueue/order_add.html',{
        'order_number' : order_number,
    })

def order_delete(request,shopID,menuboardID,order_number):
    order_complete = OrderNumber.objects.get(orderNumber=order_number)
    order_complete.delete()
    return redirect('orderingQueue:order_queue',shopID=shopID,menuboardID=menuboardID)

def order_queue(request,shopID,menuboardID):
    menuboard = MenuBoard.objects.get(menuBoardID=menuboardID)
    order_list = OrderNumber.objects.all().filter(menuBoard=menuboard)
    return render(request,'orderingQueue/order_list.html',{
        'shopID' : shopID,
        'menuboardID' : menuboardID,
        'order_list' : order_list,
    })
