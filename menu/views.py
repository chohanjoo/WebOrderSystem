from django.shortcuts import render,redirect
from .forms import MenuForm
from .models import Menu

# Create your views here.

def drink_list(request):
    menu_list = Menu.objects.all()
    return render(request,'menu/index.html',{'menu_list':menu_list})

def add_menu(request):

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu:list')

    else :
        form = MenuForm()
    return render(request,'menu/add_menu.html', {'form':form})


def menu_detail(request,pk):
    menu_detail = Menu.objects.get(pk=pk)
    return render(request,'menu/product.html',{
        'menu_detail' : menu_detail,
    })