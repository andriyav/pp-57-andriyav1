from django.urls import path
from .views import register, user_list_view, log_out, user_del, index, user_view
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('authentication/', register, name='register'),
    path('user_list/', user_list_view, name='user_list'),
    path('logout/',log_out, name='logout'),
    path('user_del/', user_del, name='user_del'),
    path('', index, name='index'),
    path('user_view/', user_view, name='user_view'),

]