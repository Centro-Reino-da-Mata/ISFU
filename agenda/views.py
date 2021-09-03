from django.shortcuts import render
from django.views.generic import ListView
from .models import Agenda


class AddAgenda(ListView):
    model = Agenda
    template_name = 'agenda.html'
