from django.shortcuts import render
from .models import Cerro
from django.views.generic import ListView, DetailView, CreateView



class CerrosListAll(ListView):
    """ Lista todos los objetos Cerros """

    template_name = 'cerro/list-all-cerros.html'
    model = Cerro
    context_object_name = 'cerros'


class CerrosDetailView(DetailView):
    """ Muestra el detalle del cerro """

    template_name = 'cerro/detail-cerro.html'
    model = Cerro

    def get_context_data(self, **kwargs):
        
        context = super(CerrosDetailView,self).get_context_data(**kwargs)
        context['label'] = 'Cerro'

        return context
 

class CerroCreateView(CreateView):
    template_name = "cerro/create-view.html"
    model = Cerro



    