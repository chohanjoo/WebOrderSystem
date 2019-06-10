from django import forms

from .models import MenuBoard,Shop

class MenuBoardForm(forms.ModelForm):

    class Meta:
        model = MenuBoard
        fields = ('menuBoardName','shopID')

class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('shopName',)