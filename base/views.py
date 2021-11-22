from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Contacto
from .forms import ContactForm

def galeria(request):
    return render(request, 'galeria.html', {})

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '/'
  