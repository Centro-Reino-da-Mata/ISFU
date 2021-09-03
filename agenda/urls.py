from django.urls import path

from .views import AddAgenda


urlpatterns = [
    path('agenda/', AddAgenda.as_view(), name='agenda')
]