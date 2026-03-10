from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'travels'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('note/<int:id>/', views.detail, name='detail'),
    path('note/create/', views.create_note, name='create_note'),
    path('note/<int:id>/update/', views.update_note, name='update_note'),
    path('note/<int:id>/delete/', views.delete_note, name='delete_note'),
]
