from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forms import PersonForm
from models import Person, Image
from datetime import datetime, timedelta
from django.utils import timezone

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'key': "value" })

def MyGallery(request):
	images = Image.objects.all()
	return render(request, 'gallery.html', {'images': images})

def GetSession(request, id):
	request.session['x'] = request.session.get('x',0) + 1
	request.session['y'] = request.session.get('y',0) + 1
	if request.session['x']==1:
		exp = timezone.localtime(timezone.now())  +timedelta(seconds=10)
		request.session.set_expiry( 10 )
	message="x: %s, y: %s"%( request.session['x'], request.session['y'] )
	print message
	return render(request, 'show_session.html',
		{
			'message': message,
			'server_datetime_local': timezone.localtime( timezone.now() ).isoformat(),
			'expiry_datetime_local': timezone.localtime( request.session.get_expiry_date() ).isoformat(),
			'expiry_datetime_utc': request.session.get_expiry_date().isoformat(),
			'id': id

		})


class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class ListPersonView(ListView):
    model = Person
    template_name='person_list.html'
