from django.urls import path
from .views import  author_list_view, author_del, AddAuthor


urlpatterns = [
    path('create_author/', AddAuthor.as_view(), name='create_author'),
    path('author_list/', author_list_view, name='author_list'),
    path('author_del/', author_del, name='author_del'),

    ]