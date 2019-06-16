from django.urls import path
from . import views

app_name = 'orderingQueue'

urlpatterns = [
    path('<int:shopID>/<int:menuboardID>/',views.order_add, name='order_add'),
    path('<int:shopID>/<int:menuboardID>/delete/<int:order_number>/', views.order_delete, name='order_delete'),
    path('<int:shopID>/<int:menuboardID>/queue/', views.order_queue, name='order_queue'),
]
