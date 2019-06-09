from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('join', views.signup, name='join'),
    path('login', views.signin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('profile/<int:pk>/',views.profile, name='profile'),
]