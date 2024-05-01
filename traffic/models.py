from django.contrib.auth.models import User
from django.db import models


class TrafficOfficer(models.Model):
    name = models.CharField(max_length=100)
    badge_number = models.IntegerField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate_number


class TrafficViolation(models.Model):
    plate_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    officer = models.ForeignKey(TrafficOfficer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate_number
