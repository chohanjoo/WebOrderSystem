from django.shortcuts import render,redirect
from .forms import MenuForm,CategoryForm
from .models import Menu,Category
from owner.models import Shop,MenuBoard

# Create your views here.

def drink_list(request,shopID,menuboardID):
    shop = Shop.objects.get(shopID=shopID)
    menuboard = MenuBoard.objects.get(menuBoardID=menuboardID)
    menu_list = Menu.objects.all()
    category_list = Category.objects.all().filter(menuBoard=menuboard)
    return render(request,'menu/index.html',{
        'menu_list':menu_list,
        'category_list' : category_list,
        'shopID' : shopID,
        'menuboardID' : menuboardID,
        })
        
def drink_list_category(request,shopID,menuboardID,categoryID):
    shop = Shop.objects.get(shopID=shopID)
    menuboard = MenuBoard.objects.get(menuBoardID=menuboardID)
    category = Category.objects.get(pk=categoryID)
    menu_list = Menu.objects.all().filter(category=category)
    category_list = Category.objects.all().filter(menuBoard=menuboard)
    return render(request,'menu/index.html',{
        'menu_list':menu_list,
        'category_list' : category_list,
        'shopID' : shopID,
        'menuboardID' : menuboardID,
        })


def add_menu(request,shopID,menuboardID):

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu:list',shopID=shopID,menuboardID=menuboardID)

    else :
        form = MenuForm()
    return render(request,'menu/add_menu.html', {'form':form,
    })


def menu_detail(request,shopID,menuboardID,pk):
    menu_detail = Menu.objects.get(pk=pk)
    menuboard = MenuBoard.objects.get(menuBoardID=menuboardID)
    category_list = Category.objects.all().filter(menuBoard=menuboard)
    return render(request,'menu/product.html',{
        'menu_detail' : menu_detail,
        'category_list' : category_list,
        'shopID' : shopID,
        'menuboardID' : menuboardID,
    })