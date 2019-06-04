from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('join', views.signup, name='join'),
    path('login', views.signin, name='login'),
]