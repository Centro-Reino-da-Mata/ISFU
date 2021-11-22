from django import forms
from base.models import Contacto


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ("__all__")
        
        