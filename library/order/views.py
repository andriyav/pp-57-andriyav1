from datetime import datetime, timedelta
from urllib import request

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Order
from authentication.models import CustomUser
from author.models import Author
from django.contrib import messages

def create_order(request):

    if request.method == 'GET':
        book_id = request.GET.get('book_id')
        print(book_id)
        book = get_object_or_404(Book, id=book_id)
        user = request.user
        end_at = None
        plated_end_at = datetime.now() + timedelta(days=15)
        order = Order.objects.create(
            book=book,
            user=user,
            end_at=end_at,
            plated_end_at=plated_end_at
        )
        order.save()
        messages.warning(request, f"Замовлення книги '{book.name}' виконане")
        return redirect('book_list')
    else:
        return render(request, 'create_order.html')


def order_list(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            user_id = int(request.POST.get('user_id'))
            print(user_id)
            user = CustomUser.objects.get(id=user_id)
            orders = Order.objects.filter(user=user).order_by('id')
        else:
            orders = Order.objects.all().order_by('id')
    else:
        orders = Order.objects.filter(user=request.user).order_by('id')
    context = {
        'orders': orders
    }
    return render(request, 'order/order_list.html', context)

def order_del(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(pk=order_id)
        order.delete()
        return redirect('order_list')

def close_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(pk=order_id)
        order.end_at = datetime.now()
        order.save()

        return redirect('order_list')
