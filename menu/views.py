from django.shortcuts import render,redirect
from .forms import MenuForm

# Create your views here.

def drink_list(request):
    return render(request,'menu/index.html')

def add_menu(request):

    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu:list')

    else :
        form = MenuForm()
    return render(request,'menu/add_menu.html', {'form':form})