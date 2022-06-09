from django.contrib import admin
from logistic_service.models import Logistician, District, Order, Car, Driver, Street, Waybill, Manufacturer_Model, City, Profile, Region


class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'lastname',
        'phone_number',
        'state',
    )



admin.site.register(Logistician)
admin.site.register(District)
admin.site.register(Order)
admin.site.register(Car)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Street)
admin.site.register(Waybill)
admin.site.register(Manufacturer_Model)
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Region)
