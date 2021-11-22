from django.urls import path

from .views import galeria, ContactCreateView


urlpatterns = [
    path('galeria/', galeria, name='galeria'),
    path('contacto/', ContactCreateView.as_view(), name='contacto'),
]