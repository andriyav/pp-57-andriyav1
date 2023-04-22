from django.shortcuts import render, redirect
from author.models import Author
from book.models import Book
from django.contrib import messages

def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        if not patronymic:
            patronymic = '-'

        author = Author.create(name, surname, patronymic)
        return redirect('author_list')
    else:
        return render(request, 'author/author_list.html')

def author_list_view(request):

    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/author_list.html', context)

def author_del(request):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        author = Author.objects.get(pk=author_id)
        book = Book.objects.filter(authors=author)
        if book:
            messages.warning(request, "Ви не можете видалити автора при наявності книги в бібліотеці")
        else:
            author.delete()
        return redirect('author_list')
