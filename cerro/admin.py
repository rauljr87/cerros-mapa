from django.contrib import admin
from .models import Cerro, Latitud, Longitud


class CerroAdmin(admin.ModelAdmin):
    """ Display fields of the model class Cerro """

    list_display = (
        'name',
        'longitud',
        'latitud',
    )
    search_fields = ('name',)
    list_filter = ('name',)


class LatitudAdmin(admin.ModelAdmin):
    """ Display fields of the model class Latitud """

    list_display = (
        'degrees',
        'minutes',
        'seconds',
        'get_direction_display',
    )


class LongitudAdmin(admin.ModelAdmin):
    """ Display fields of the model class Latitud """

    list_display = (
        'degrees',
        'minutes',
        'seconds',
        'get_direction_display',
    )


admin.site.register(Cerro, CerroAdmin)
admin.site.register(Latitud, LatitudAdmin)
admin.site.register(Longitud, LongitudAdmin)
