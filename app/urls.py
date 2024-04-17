from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('reserva_ingresso/', views.reserva_ingresso, name='reserva_ingresso')
]