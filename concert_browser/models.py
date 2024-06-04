from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

class Location(models.Model):
    nazwa = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)
    miasto = models.CharField(max_length=100)
    kod_pocztowy = models.CharField(max_length=10)

    def __str__(self):
        return self.nazwa

class Concert(models.Model):
    nazwa = models.CharField(max_length=255)
    data = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='concerts')
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_concerts')

    def __str__(self):
        return self.nazwa
