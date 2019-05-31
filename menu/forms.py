from django import forms

from .models import Menu, Category

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('name', 'price','image','category')

# class MenuBoardForm(forms.ModelForm):

#     class Meta:
#         model = Menu
#         fields = ('name', 'price','image','category')

# class CategoryForm(forms.ModelForm):

#     class Meta:
#         model = Menu
#         fields = ('name', 'price','image','category')

# class ShopForm(forms.ModelForm):

#     class Meta:
#         model = Menu
#         fields = ('name', 'price','image','category')