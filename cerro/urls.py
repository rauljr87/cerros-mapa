from django.urls import path
from .views import CerrosListAll, CerrosDetailView


app_name = 'cerro_app'


urlpatterns = [
    path('list-all-cerros/', CerrosListAll.as_view(), name='list-all-cerros'),
    path('detail-cerro/<pk>/', CerrosDetailView.as_view(), name='detail-cerro'),
]
