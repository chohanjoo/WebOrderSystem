from django.shortcuts import render,redirect
from .forms import MenuBoardForm
from .models import MenuBoard
import random
from menu.models import Menu
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# Create your views here.

def index(request):
    menuboard_list = MenuBoard.objects.all()
    if request.method == "POST":
        form = MenuBoardForm(request.POST)
        if form.is_valid():
            menuboard = form.save(commit=False)
            menuboard.menuBoardID = random.randrange(1000000000000000000, 9223372036854775807)
            # menuboard.menuBoardID = urlsafe_base64_encode(force_bytes(menuboard.pk))
            menuboard.save()
            return redirect('owner:index')
    else:
        form = MenuBoardForm()
    return render(request,'owner/index.html',
            {'form':form,
             'menuboard_list':menuboard_list})

def create_menuboard(request):
    pass
    
def edit_menuboard(request):
    menu_list = Menu.objects.all()
    return render(request,'menu/index_edit.html',{'menu_list':menu_list})




from django.views.generic import TemplateView
from django_popup_view_field.registry import registry_popup_view

class ColorsPopupView(TemplateView):
    template_name = 'owner/popup.html'

# REGISTER IS IMPORTANT
registry_popup_view.register(ColorsPopupView)