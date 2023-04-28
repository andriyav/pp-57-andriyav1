from django.urls import path
from .views import  book_list, filter_books, book_del, book_view, create_book

urlpatterns = [
    path('create_book/', create_book, name='create_book'),
    path('book_list/', book_list, name='book_list'),
    path('filter_books/', filter_books, name='author_sort'),
    path('book_del/', book_del, name='book_del'),
    path('book_view/', book_view, name='book_view'),
    ]