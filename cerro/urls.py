from django.urls import path
from .views import ListAllCerros, DetailViewCerros


app_name = 'cerro_app'


urlpatterns = [
    path('list-all-cerros/', ListAllCerros.as_view(), name='list-all-cerros'),
    path('detail-cerro/<pk>/', DetailViewCerros.as_view(), name='detail-cerro'),
]
