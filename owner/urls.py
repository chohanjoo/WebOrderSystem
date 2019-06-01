from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/menuboard', views.create_menuboard, name='create_menuboard'),
    path('edit/menuboard', views.edit_menuboard, name='edit_menuboard'),
    
]
