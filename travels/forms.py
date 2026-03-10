from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import TravelNote

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True, label='Почта')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

class TravelNoteForm(forms.ModelForm):
    class Meta:
        model = TravelNote
        fields = ['place_name', 'country', 'date_of_trip', 'description', 'photo']
        widgets = {
            'date_of_trip': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'place_name': 'Место',
            'country': 'Страна',
            'date_of_trip': 'Дата поездки',
            'description': 'Описание поездки',
            'photo': 'Загрузить фото',
        }
