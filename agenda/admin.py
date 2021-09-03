from django.contrib import admin
from .models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_actividad', 'state')

admin.site.register(Agenda, AgendaAdmin)