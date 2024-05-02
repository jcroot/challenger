from django.contrib.auth.models import User
from django.db import models


class TrafficOfficer(models.Model):
    class Meta:
        db_table = 'traffic_officer'

    badge_number = models.IntegerField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Person(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate_number


class TrafficViolation(models.Model):
    class Meta:
        db_table = 'traffic_violation'

    plate_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    officer = models.ForeignKey(TrafficOfficer, on_delete=models.CASCADE)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.plate_number
