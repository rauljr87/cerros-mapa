from django.db import models


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

    def __str__(self):
        return str(self.id) + ' - ' + str(self.degrees) + '°' + str(self.minutes) + """'""" + str(
            self.seconds) + '''"''' + self.direction


class Longitud(models.Model):
    """ Longitud de coordenada """

    DIR_CHOICES = (
        ('0', 'E'),
        ('1', 'W'),
    )
    degrees = models.IntegerField('Grados')
    minutes = models.IntegerField('Minutes')
    seconds = models.IntegerField('Seconds')
    direction = models.CharField('Directions', max_length=10, choices=DIR_CHOICES)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.degrees) + '°' + str(self.minutes) + """'""" + str(
            self.seconds) + '''"''' + self.direction


class Cerros(models.Model):
    """ Tabla para nombres de cerros """

    name = models.CharField('Nombre del Cerro', max_length=50)
    latitud = models.OneToOneField(
        Latitud,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    longitud = models.OneToOneField(
        Longitud,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return str(self.id) + ' - ' + self.name
