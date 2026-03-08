from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'travels'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('note_detail/<int:id>', views.detail, name='detail')
]
