from django.urls import path
from .views import create_author, author_list_view, author_del

urlpatterns = [
    path('create_author/', create_author, name='create_author'),
    path('author_list/', author_list_view, name='author_list'),
    path('author_del/', author_del, name='author_del'),

    ]