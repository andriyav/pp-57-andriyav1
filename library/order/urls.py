from django.urls import path
from .views import create_order, order_list, order_del, close_order

urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('order_list/', order_list, name='order_list'),
    path('close_order/', close_order, name='close_order'),
    path('order_del/', order_del, name='order_del'),

    ]