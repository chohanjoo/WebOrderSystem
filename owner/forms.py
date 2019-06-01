from django import forms

from .models import MenuBoard

class MenuBoardForm(forms.ModelForm):

    class Meta:
        model = MenuBoard
        fields = ('menuBoardName','shopID')