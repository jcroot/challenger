from django.contrib import admin

from .models import TrafficOfficer, Person, Vehicle, TrafficViolation

admin.site.register(TrafficOfficer)
admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(TrafficViolation)
