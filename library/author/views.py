from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Author
from book.models import Book
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CreateAuthor


class AddAuthor(CreateView):
    form_class = CreateAuthor
    template_name = 'author/author_create.html'
    success_url = reverse_lazy('author_list')


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


