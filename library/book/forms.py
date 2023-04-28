from django import forms


class BookForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Назва'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Опис',
        }))
    count = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Кількість',
        }))
