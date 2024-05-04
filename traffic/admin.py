from django.contrib import admin

from .models import TrafficOfficer, Person, Vehicle, TrafficViolation, CarBrand


class TrafficUserAdmin(admin.ModelAdmin):
    list_display = ('badge_number', 'fullname', 'email_address')

    @admin.display(description='Fullname')
    def fullname(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    @admin.display(description='Email Address')
    def email_address(self, obj):
        return f'{obj.user.email}'


class VehicleInline(admin.TabularInline):
    model = Vehicle
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    inlines = [
        VehicleInline,
    ]


class TrafficViolationAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'vehicle_belongs_to', 'officer', 'comments', 'timestamp')
    list_filter = ('plate_number', 'officer')
    search_fields = ('vehicle__plate_number', 'officer__badge_number', 'comments')

    @admin.display(description='Belongs to')
    def vehicle_belongs_to(self, obj):
        return obj.plate_number.owner.full_name


admin.site.register(TrafficOfficer, TrafficUserAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Vehicle)
admin.site.register(TrafficViolation, TrafficViolationAdmin)
admin.site.register(CarBrand)
