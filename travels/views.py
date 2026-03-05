from django.shortcuts import render, redirect, get_object_or_404
from .models import TravelNote


def home(request):
    if request.user.is_authenticated:
        notes = TravelNote.objects.filter(author=request.user).order_by('created_at')[:5]
        return render(request, 'travels/home.html', context={'notes': notes})
    return render(request, 'travels/home.html')

def dashboard(request):
    return render(request, 'travels/dashboard.html')

