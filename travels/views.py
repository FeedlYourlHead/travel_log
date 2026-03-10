from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import TravelNote
from .forms import RegisterForm, TravelNoteForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    if request.user.is_authenticated:
        notes = TravelNote.objects.filter(author=request.user).order_by('-created_at')[:5]
        return render(request, 'travels/home.html', context={'notes': notes})
    return render(request, 'travels/home.html')

@login_required
def dashboard(request):
    notes = TravelNote.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'travels/dashboard.html', context={'notes': notes})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('travels:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'travels/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('travels:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'travels/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return redirect('travels:home')

@login_required
def detail(request, id):
    note = get_object_or_404(TravelNote, id=id, author=request.user)
    return render(request, 'travels/note_detail.html', {'note': note})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = TravelNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, 'Запись успешно создана!')
            return redirect('travels:detail', id=note.id)
    else:
        form = TravelNoteForm()
    return render(request, 'travels/note_form.html', {'form': form, 'title': 'Добавить поездку'})

@login_required
def update_note(request, id):
    note = get_object_or_404(TravelNote, id=id, author=request.user)
    if request.method == 'POST':
        form = TravelNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обновлена!')
            return redirect('travels:detail', id=note.id)
    else:
        form = TravelNoteForm(instance=note)
    return render(request, 'travels/note_form.html', {'form': form, 'title': 'Редактировать поездку'})

@login_required
def delete_note(request, id):
    note = get_object_or_404(TravelNote, id=id, author=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Запись удалена')
        return redirect('travels:dashboard')
    return render(request, 'travels/note_confirm_delete.html', {'note': note})
