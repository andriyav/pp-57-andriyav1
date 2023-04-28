from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import CustomUser
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user_email = registerForm.cleaned_data['email']
            user_password = registerForm.cleaned_data['password']
            user.email = user_email
            user.set_password(user_password)
            if user.role == 1:
                user.is_superuser = True
            user.is_active = True
            user.save()
            user_log = authenticate(username=user_email, password=user_password)
            if user is not None:
                login(request, user_log)
                return redirect('index')
            else:
                messages.error(
                    request,
                    'Сталися помика. Перевірте дані ще раз'
                )
                return redirect('register')
    else:
        registerForm = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': registerForm})


def user_list_view(request):
    users = CustomUser.objects.all().order_by('id')
    context = {
        'users': users
    }
    return render(request, 'authentication/user_list.html', context)


def log_out(request):
    logout(request)
    return redirect('index')


def user_del(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(pk=user_id)
        user.delete()
        return redirect('user_list')


def index(request):
    return render(request, 'authentication/index.html')


def user_view(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        user = CustomUser.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'authentication/user_view.html', context)
