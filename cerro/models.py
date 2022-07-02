from django.db import models


class Latitud(models.Model):
    """ Latitud de coordenada """

    DIRECTIONS = (
        ('0', 'N'),
        ('1', 'S'),
    )
    degrees = models.IntegerField('Grados')
    minutes = models.IntegerField('Minutes')
    seconds = models.FloatField('Seconds')
    direction = models.CharField('Directions', max_length=10, choices=DIRECTIONS)

    class Meta:
        verbose_name = 'Latitud'
        verbose_name_plural = 'Latitudes'

    def __str__(self):
        return str(self.degrees) + '°' + str(self.minutes) + """'""" + str(
            self.seconds) + '''"''' + self.get_direction_display()


class Longitud(models.Model):
    """ Longitud de coordenada """

    DIRECTIONS = (
        ('0', 'E'),
        ('1', 'W'),
    )
    degrees = models.IntegerField('Grados')
    minutes = models.IntegerField('Minutes')
    seconds = models.FloatField('Seconds')
    direction = models.CharField('Directions', max_length=10, choices=DIRECTIONS)

    class Meta:
        verbose_name = 'Longitud'
        verbose_name_plural = 'Longitudes'

    def __str__(self):
        return str(self.degrees) + '°' + str(self.minutes) + """'""" + str(
            self.seconds) + '''"''' + self.get_direction_display()



class Cerro(models.Model):
    """ Tabla para nombres de cerros """

    name = models.CharField('Nombre del Cerro', max_length=50)
    latitud = models.OneToOneField(
        Latitud,
        on_delete=models.CASCADE,
    )
    longitud = models.OneToOneField(
        Longitud,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Cerro'
        verbose_name_plural = 'Cerros del Ecuador'

    def __str__(self):
        return str(self.id) + ' - ' + self.name
