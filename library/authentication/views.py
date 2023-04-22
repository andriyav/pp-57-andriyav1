from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from authentication.models import CustomUser


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        if role == '1':
            is_staff = True
        else:
            is_staff = False

        # Check if user already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Такий логін вже існує')
            return redirect('register')
        else:
            if is_staff:
                user = CustomUser.objects.create_superuser(
                    email=email,
                    password=password,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    role=role,
                    is_staff=is_staff
                )
            else:
                user = CustomUser.objects.create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    role=role,
                    is_staff=is_staff
                )

            # user = authenticate(username=email, password=password)
            print(email, password, user)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(
                    request,
                    'Сталися помика. Перевірте дані ще раз'
                )
                return redirect('register')

    else:
        return render(request, 'authentication/register.html')


def user_list_view(request):
    users = CustomUser.objects.all().order_by('id')
    context = {
        'users': users
    }
    return render(request, 'authentication/user_list.html', context)


def log_out(request):
    logout(request)
    return redirect('index')


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(
                request,
                'Такий користувач не зареєстрований'
            )
    return render(request, 'authentication/login.html')


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
    print(context)
    return render(request, 'authentication/user_view.html', context)
