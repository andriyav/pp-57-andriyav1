from django import forms
from .models import Author


class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = 'surname','name', 'surname', 'patronymic'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' , "placeholder": "Ім'я"}),
            'surname': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Прізвище"}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control', "placeholder": "По батькові"})
        }

