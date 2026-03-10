from django.contrib import admin
from .models import TravelNote


@admin.register(TravelNote)
class TravelNoteAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'country', 'date_of_trip', 'author', 'created_at')
    list_filter = ('country', 'date_of_trip', 'created_at')
    search_fields = ('place_name', 'country', 'description', 'author__username')
    date_hierarchy = 'date_of_trip'
