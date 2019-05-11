from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})#rendering through Django templates

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})#rendering through Django templates

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})#rendering through Django templates
