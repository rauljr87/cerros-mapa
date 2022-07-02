from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Cerro


class CerroForm(forms.ModelForm):
    """ Formulario para crear un nuevo cerro """

    class Meta:
        model = Cerro
        fields = (
            'name',
            'latitud',
            'longitud',
        )
