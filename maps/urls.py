from django.urls import path
from . import views


app_name = 'maps_app'


urlpatterns = [
    # path('mapview/', views.cerro_map, name='mapview'),
    # pasamos id por url
    path('mapview/<str:id>/', views.cerro_map, name='mapview'),
]
