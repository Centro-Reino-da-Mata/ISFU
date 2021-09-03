from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Agenda(models.Model):
    title = models.CharField('Título', max_length=120)
    description = models.CharField('Descripción', max_length=120)
    date_agenda = models.DateField('Fecha de creación', auto_now=False , auto_now_add=True)
    date_actividad = models.DateTimeField('Fecha de Actividad', auto_now=False, auto_now_add=False, blank=True, null=True)
    state = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return self.title
