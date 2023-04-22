from urllib import request

from django.shortcuts import render, redirect
from .models import Book
from author.models import Author

def book_list(request):
    book_list = Book.objects.all()

    title = request.GET.get('title')

    if title == 'title_n':
        books = book_list.order_by('name')
    elif title == 'title_r':
        books = book_list.order_by('-name')

    elif title == 'id_n':
        books = book_list.order_by('id')
    elif title == 'id_r':
        books = book_list.order_by('-id')

    elif title == 'description_n':
        books = book_list.order_by('description')
    elif title == 'description_r':
        books = book_list.order_by('-description')

    elif title == 'count_n':
        books = book_list.order_by('count')
    elif title == 'count_r':
        books = book_list.order_by('-count')

    elif title == 'author_n':
        books = book_list.order_by('authors')
    elif title == 'author_r':
        books = book_list.order_by('-authors')
    else:
        books = Book.get_all()
    authors1 = Author.objects.all()
    return render(request, 'book/book_list.html', {'books': books, 'authors1':authors1})


def filter_books(request):
    author_name = request.GET.get('author_name')
    title = request.GET.get('title')

    books = Book.objects.filter(name__contains=title, authors__name__contains=author_name)
    return render(request, 'books.html', {'books': books})

def show_books_by_user(user_id):
    books = Book.objects.filter(users__id=user_id)
    return render(request, 'books.html', {'books': books})


def create_book(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        count = request.POST.get('count')
        authors_id = request.POST.get('authors')

        book = Book.objects.create(name=name, description=description, count=count)

        author = Author.objects.get(id=authors_id)

        book.authors.add(author)
        book.save()
        return redirect('book_list')
    context = {'authors': authors}
    return render(request, 'book/book_list.html', context)

def book_del(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        order = Book.objects.get(pk=book_id)
        order.delete()
        return redirect('book_list')

def book_view(request):
    authors = Author.objects.all()
    if request.method == 'GET':

        book_id = request.GET.get('book_id')
        print(book_id)
        books_view = Book.objects.get(pk=book_id)
    context = {'books_view': books_view, 'authors': authors }
    print(context)
    return render(request, 'book/book_view.html', context)

