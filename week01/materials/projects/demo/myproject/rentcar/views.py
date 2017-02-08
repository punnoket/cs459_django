from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render
from forms import CustomerForm
from models import Customer, Car
import datetime
class CreateCustomerView(CreateView):
	queryset = Customer()
	template_name='customer.html'
	form_class = CustomerForm
	success_url = '/'
	
class UpdateCustomerView(UpdateView):
	queryset = Customer.objects.all()
	template_name='customer.html'
	form_class = CustomerForm
	success_url = '/'

def home(request):
	return render(request, 'home.html', {'mytime:': "+-+" })

class ListCarView(ListView):
    model = Car
    template_name='car_list.html'

# Create your views here.
