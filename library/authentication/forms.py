from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Логін'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
        }
    ))


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password', 'role')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-control", "placeholder": "Ім'я"}),
            'middle_name': forms.TextInput(attrs={'class': "form-control", "placeholder": "По батькові"}),
            'last_name': forms.TextInput(attrs={'class': "form-control", "placeholder": "Прізвище"}),
            'email': forms.EmailInput(attrs={'class': "form-control", "placeholder": "email"}),
            'password': forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Пароль"}),

        }
