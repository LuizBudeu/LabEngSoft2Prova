from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserva_ingresso, name='reserva_ingresso'),
    path('reserva_ingresso/', views.reserva_ingresso, name='reserva_ingresso'),
    path('get_ingressos/', views.get_ingressos, name='get_ingressos')
]