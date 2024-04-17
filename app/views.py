from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.http import HttpRequest
from datetime import datetime
from datetime import date

from django.shortcuts import render, redirect

from .models import Ingresso

def reserva_ingresso(request: HttpRequest):
    ingressos_disponiveis = list(pega_ingressos_disponiveis().values())
    return render(request, 'reserva_ingresso.html', {'ingressos_disponiveis':ingressos_disponiveis})


@api_view(['GET'])
def get_ingressos(request: HttpRequest) -> Response:
    ingressos = Ingresso.objects.all().values()
    return Response(ingressos)


def pega_ingressos_disponiveis():
    return  Ingresso.objects.filter(
        status=0
    )


def reserva_ingresso(request: HttpRequest):
    if request.method == 'POST':
        nome_usuario = request.POST['nome']
        numero_ids = request.POST.getlist('numero_ids')

        for num_id in numero_ids:
                
            ingresso = Ingresso.objects.get(
                numero=num_id
            )
            ingresso.status = 1
            ingresso.nome_usuario = nome_usuario
            ingresso.save()


    ingressos_disponiveis = list(pega_ingressos_disponiveis().values())
    return render(request, 'reserva_ingresso.html', {'ingressos_disponiveis':ingressos_disponiveis})