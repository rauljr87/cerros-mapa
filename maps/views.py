from multiprocessing import context
import re
from unicodedata import name
from cerro.models import Cerro
from django.shortcuts import render
from cerro.utils import get_latitud_decimal, get_longitud_decimal
import folium


def cerro_map(request, id):
    """ Geolocliza un cerro específico, recibe id por url """
    
    # id = 5
    mymap = folium.Map (location = [ -1.831239, -78.183406],  zoom_start=7)
    
    folium.TileLayer('openstreetmap').add_to(mymap)
    
    tooltip = Cerro.objects.get(pk=id)
    lat = get_latitud_decimal(id=id)
    lon = get_longitud_decimal(id=id)
    popup='popup'
    
    folium.Marker([lat, lon], popup=popup, tooltip=tooltip).add_to(mymap)

    m = mymap._repr_html_()

    context = {'my_map': m}

    return render(request, 'maps/mapview.html', context)

