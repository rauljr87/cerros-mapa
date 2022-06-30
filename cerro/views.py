from django.shortcuts import render
from .models import Cerro
from django.views.generic import ListView, DetailView


class ListAllCerros(ListView):
    """ Lista todos los objetos Cerros """

    template_name = 'cerro/list-all-cerros.html'
    model = Cerro
    context_object_name = 'cerros'


class DetailViewCerros(DetailView):
    """ Muestra el detalle del cerro """

    template_name = 'cerro/detail-cerro.html'
    model = Cerro

    def get_context_data(self, **kwargs):
        
        context = super(DetailViewCerros,self).get_context_data(**kwargs)
        context['label'] = 'Cerro'

        return context 
