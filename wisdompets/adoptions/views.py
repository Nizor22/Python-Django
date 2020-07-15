from django.shortcuts import render
from django.http import Http404

from .models import Pet


# Display the home.html page if a specific pet had not been in the requested URL.
def home(request):
	pets = Pet.objects.all()
	return render(request, 'home.html', {
		'pets': pets,
	})


# If a specific page had been selected check if the pet exists
# display that pet's page. Otherwise raise an Exception to display an Error404 page.
def pet_detail(request, pet_id):
	try:
		pet = Pet.objects.get(id=pet_id)
	except Pet.DoesNotExist:
		raise Http404('pet not found')
	return render(request, 'pet_detail.html', {
		'pet': pet,
	})
