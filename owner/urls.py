from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('<int:pk>/',views.index, name='index'),
    path('<int:pk>/create/shop/',views.create_shop, name='create_shop'),
    path('create/menuboard/', views.create_menuboard, name='create_menuboard'),
    path('<int:pk>/edit/menuboard/<int:menuboard_id>/', views.edit_menuboard, name='edit_menuboard'),
    path('<int:pk>/edit/menuboard/<int:menuboard_id>/add/category/', views.add_category, name='add_category'),
    
]
