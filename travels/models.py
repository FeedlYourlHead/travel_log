from django.db import models
from django.contrib.auth.models import User

class TravelNote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_of_trip = models.DateField()
    description = models.TextField()
    photo = models.ImageField()
    created_at = models.DateField(auto_now=True)

