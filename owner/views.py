from django.shortcuts import render,redirect
from .forms import MenuBoardForm,ShopForm
from .models import MenuBoard,Shop
import random
from menu.models import Menu,Category
from menu.forms import MenuForm,CategoryForm
from django.contrib.auth.models import User
from datetime import datetime


# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# Create your views here.

def index(request,pk):
    user = User.objects.get(pk=pk)
    shop = Shop.objects.all().filter(user=user)
    menuboard_list = MenuBoard.objects.all()#.filter(shopID=shop.shopID)
    if request.method == "POST":
        form = MenuBoardForm(request.POST)
        if form.is_valid():
            menuboard = form.save(commit=False)
            menuboard.menuBoardID = random.randrange(1000000000000000000, 9223372036854775807)
            # menuboard.menuBoardID = urlsafe_base64_encode(force_bytes(menuboard.pk))
            menuboard.save()
            return redirect('owner:index',pk=user.pk)
    else:
        form = MenuBoardForm()
        shop_form = ShopForm()
    return render(request,'owner/index.html',
            {'form':form,
             'menuboard_list':menuboard_list,
             'shop_list':shop,
             'shop_form' : shop_form,
             })

def create_shop(request,pk):
    menuboard_list = MenuBoard.objects.all()
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=pk)
            shop = form.save(commit=False)
            shop.shopID = random.randrange(1, 900000000000000000)
            shop.user = user
            shop.openDate = datetime.today()            # 현재 날짜 가져오기 
            shop.save()
            return redirect('owner:index', pk=user.pk)
    else:
        form = ShopForm()
    return render(request, 'owner/index.html',{
        'form' : form,
        'menuboard_list':menuboard_list
    })
            


def create_menuboard(request):
    pass
    
def edit_menuboard(request):
    menu_list = Menu.objects.all()
    category_list = Category.objects.all()
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            new_menu = form.save(commit=False)
            new_menu.save()
            return redirect('owner:edit_menuboard')
    else:
        form = MenuForm()
        category_form = CategoryForm()
    return render(request,'menu/index_edit.html',
            {'menu_list':menu_list,
             'category_list' : category_list,
             'form' : form,
             'category_form' : category_form,
              })



def add_category(request):
    menu_list = Menu.objects.all()
    category_list = Category.objects.all()
    if request.method == "POST" :
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.save()
            return redirect('owner:edit_menuboard')
    else:
        form = CategoryForm()
    return render(request,'menu/index_edit.html',{
        'menu_list' : menu_list,
        'category_list' : category_list,
        'form' : form,
    })


from django.views.generic import TemplateView
from django_popup_view_field.registry import registry_popup_view

class ColorsPopupView(TemplateView):
    template_name = 'owner/popup.html'

# REGISTER IS IMPORTANT
registry_popup_view.register(ColorsPopupView)