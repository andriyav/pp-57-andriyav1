from django.urls import path
from .views import register, user_list_view, log_in, log_out, user_del, index, user_view

urlpatterns = [
    path('authentication/', register, name='register'),
    path('user_list/', user_list_view, name='user_list'),
    path('login/',log_in, name='login'),
    path('logout/',log_out, name='logout'),
    path('user_del/', user_del, name='user_del'),
    path('', index, name='index'),
    path('user_view/', user_view, name='user_view'),

]