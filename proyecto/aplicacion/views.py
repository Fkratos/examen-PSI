"""
Federico Pérez Fernández
04-06-2021
PSI - Conv. Extraordinaria
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from aplicacion.models import (Jugador, Partida, Movimiento)
from django.urls import reverse

def index(request):
    string = "Examen Convocatoria Extraordinaria PSI 2020 - 2021 " \
             "<br>Federico Pérez Fernández" \
             "<br>NIA: 382898" \
             "<br>Fecha: DD-MM-YYYY" \
             "<hr>" \
             "<br><a href=\"aplicacion/jugador\">Pagina Jugador</a>"

    return HttpResponse(string)

def jugador(request):
    context_dict = {}

    try:  # Buscamos al jugador con id 1002
        jugador = Jugador.objects.get(id=1002)
    except Jugador.DoesNotExist:  # El jugador no existe
        print("###### Error Message: Jugador no encontrado!")
        # Anyade el mensaje de error
        context_dict['error'] = 'Usuario no encontrado!'
        # Volvemos a la pagina de inicio
        return render(request, 'aplicacion/jugador.html', context_dict)

    context_dict['nombreJ'] = jugador.nombreJ
    context_dict['movimientos'] = Movimiento.objects.filter(jugador=jugador)

    return render(request, 'aplicacion/jugador.html', context_dict)

