from django.contrib import admin
from .models import TravelNote

admin.site.register(TravelNote)

# @admin.register(TravelNote)
# class TravelNoteAdmin(admin.ModelAdmin):
#     list_display = ('place_name', 'country', 'trip_date', 'author', 'created_at')
#     list_filter = ('country', 'trip_date', 'created_at')
#     search_fields = ('place_name', 'country', 'description')
