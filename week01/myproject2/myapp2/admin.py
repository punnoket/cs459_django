from django.contrib import admin
from .models import Customer, Car, Rent

class CustomerAdmin(admin.ModelAdmin):
	#exclude=['date_of_birth']
	list_display=[f.name for f in Customer._meta.fields]
class CarAdmin(admin.ModelAdmin):
	list_display = ['model', 'milage', 'ppd']
class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
	list_editable=['start','stop','car']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Rent,RentAdmin)