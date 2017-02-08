from django.contrib import admin
from models import Customer, Car, Rent

class CustomerAdmin(admin.ModelAdmin):
	#exclude=['date_of_birth']
	list_display=[f.name for f in Customer._meta.fields]
class CarAdmin(admin.ModelAdmin):
	fields = ['model', 'milage', 'ppd', 'image']
class RentAdmin(admin.ModelAdmin):
	exclude=[]


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Rent,RentAdmin)