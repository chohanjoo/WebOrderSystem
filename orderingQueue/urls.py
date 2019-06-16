from django.urls import path
from . import views

app_name = 'orderingQueue'

urlpatterns = [
    path('',views.order_add, name='order_add'),
    path('<int:order_number>/delete/', views.order_delete, name='order_delete'),
    path('<int:shopID>/<int:menuboardID>/queue/', views.order_queue, name='order_queue'),
]
