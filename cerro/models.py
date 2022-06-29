from django.db import models


class Cerros(models.Model):
    """ Tabla para nombres de cerros """

    name = models.CharField('Nombre del Cerro', max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Latitud(models.Model):
    """ Latitud de coordenada """

    DIR_CHOICES = (
        ('0', 'N'),
        ('1', 'S'),
    )
    degrees = models.IntegerField('Grados')
    minutes = models.IntegerField('Minutes')
    seconds = models.IntegerField('Seconds')
    direction = models.CharField('Directions', max_length=10, choices=DIR_CHOICES)
