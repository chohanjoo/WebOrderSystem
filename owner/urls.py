from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('<int:pk>/',views.index, name='index'),
    path('<int:pk>/create/shop/',views.create_shop, name='create_shop'),
    path('create/menuboard', views.create_menuboard, name='create_menuboard'),
    path('edit/menuboard', views.edit_menuboard, name='edit_menuboard'),
    
]
