from django.contrib import admin

from .models import TrafficOfficer, Person, Vehicle, TrafficViolation, CarBrand

admin.site.register(TrafficOfficer)
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(TrafficViolation)
admin.site.register(CarBrand)
