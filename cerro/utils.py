from unicodedata import decimal
from .models import Cerro

def get_latitud_decimal(id):
    """ Retorna latitud en coordenadas decimales """

    obj = Cerro.objects.get(pk=id)
    d = obj.latitud.degrees
    m = obj.latitud.minutes/60
    s = obj.latitud.seconds/(60*60)
    direction_ = obj.latitud.direction
    lat_decimal = d + m + s

    if direction_ == '1':
        lat_decimal *= -1
    
    return lat_decimal


def get_longitud_decimal(id):
    """ Retorna longitud en coordenadas decimales """

    obj = Cerro.objects.get(pk=id)
    d = obj.longitud.degrees
    m = obj.longitud.minutes/60
    s = obj.longitud.seconds/(60*60)
    direction_ = obj.longitud.direction
    lat_decimal = d + m + s

    if direction_ == '1':
        lat_decimal *= -1
    
    return lat_decimal





# self.get_direction_display()
# Cerro.objects.filter(name='Cerro Chilola')
# l = Cerro.objects.first()
# Cerro.objects.get(pk=1)
# print([e.name for e in Cerro.objects.all()])
