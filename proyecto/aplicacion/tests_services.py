"""
Federico Pérez Fernández
04-06-2021
PSI - Conv. Extraordinaria
"""

import re
from django.urls import reverse
from django.test import TestCase
from django.test import Client
from aplicacion.management.commands.poblar import Command
from aplicacion.models import (Jugador, Partida, Movimiento)

from proyecto.settings import BASE_DIR

pathToProject = BASE_DIR
LANDING_PAGE = "aplicacion:index"
PLAYER_PAGE = "aplicacion:jugador"

patternText = \
"""
                    <th>1001</th>
                    <td>Jan. 25, 2021, midnight
                    <td>Dh5
                    <td>5
"""

SERVICE_DEF = {PLAYER_PAGE: {"pattern": patternText}}

def _addPlayer(**kwargs):
    """
    Anyade un jugador a la aplicacion
    ---------------------------------
        :argument kwargs
            id = id del jugador
            nombreJ = nombre del jugador

        :return una instancia del jugador obtenido/creado
    """

    try:
        jugador = Jugador.objects.get(id=kwargs['id'])
    except Jugador.DoesNotExist:
        jugador = Jugador.objects.create(id=kwargs['id'],
                                         nombreJ=kwargs['nombreJ'])
        jugador.save()

    return jugador


def _addMatch(**kwargs):
    """
    Anyade a la aplicacion una partida
    ----------------------------------
        :argument kwargs
            id = id de la partida
            fecha = fecha de la partida
            jugadorB = instancia del jugador de fichas blancas
            jugadorN = instancia del jugador de fichas negras

        :return una instancia de la partida obtenida/creada
    """

    try:
        partida = Partida.objects.get(id=kwargs['id'])
    except Partida.DoesNotExist:
        jugadorB = Jugador.objects.get(id=kwargs['jugadorB'])
        jugadorN = Jugador.objects.get(id=kwargs['jugadorN'])
        partida = Partida.objects.create(id=kwargs['id'],
                                         fecha=kwargs['fecha'],
                                         jugadorB=jugadorB,
                                         jugadorN=jugadorN)
        partida.save()

    return partida


def _addMovement(**kwargs):
    """
        Anyade un movimiento a la partida
        ----------------------------------
            :argument kwargs
                id = id del movimiento
                jugador = instancia del jugador
                partida = instancia de la partida
                desc = descripcion del movimiento
                orden = posicion del movimiento en la secuencia de
                movimientos de la partida

            :return una instancia del movimiento obtenido/creado
    """

    try:
        movimiento = Movimiento.objects.get(id=kwargs['id'])
    except Movimiento.DoesNotExist:
        partida = Partida.objects.get(id=kwargs['partida'])
        jugador = Jugador.objects.get(id=kwargs['jugador'])
        movimiento = Movimiento.objects.create(id=kwargs['id'],
                                               partida=partida,
                                               jugador=jugador,
                                               descripcion=kwargs['desc'],
                                               orden=kwargs['orden'])

    return movimiento


class ServiceBaseTest(TestCase):
    """
    Contiene los metodos para realizar el test de la prueba de la conv.
    extraordinaria
    """

    def doCleanups(self) -> None:
        """Limpia la base de datos de la aplicacion"""
        self.client = Client()
        # load Command class from populate
        c = Command()
        # execute clean database
        c.handle(model='clean')

    def setUp(self) -> None:
        """Define los parametros de los objetos a crear"""

        # Parametros de los jugadores
        self.paramsJugador1 = {'id': 1001, 'nombreJ': 'jugador1'}
        self.paramsJugador2 = {'id': 1002, 'nombreJ': 'jugador2'}

        # Parametros de la partida
        self.paramsPartida = {'id': 1001, 'fecha': '2021-01-25',
                              'jugadorB': 1002, 'jugadorN': 1001}

        # Parametros del movimiento
        self.paramsMovimiento = {'id': 1001, 'partida': 1001,
                                 'jugador': 1002, 'desc': 'Dh5', 'orden': 5}

        # Instancia los objectos
        self.jugador1 = _addPlayer(id=self.paramsJugador1['id'],
                                   nombreJ=self.paramsJugador1['nombreJ'])
        self.jugador2 = _addPlayer(id=self.paramsJugador2['id'],
                                   nombreJ=self.paramsJugador2['nombreJ'])
        self.partida = _addMatch(id=self.paramsPartida['id'],
                                 fecha=self.paramsPartida['fecha'],
                                 jugadorB=self.paramsPartida['jugadorB'],
                                 jugadorN=self.paramsPartida['jugadorN'])
        self.movimiento = _addMovement(id=self.paramsMovimiento['id'],
                                       partida=self.paramsMovimiento[
                                           'partida'],
                                       jugador=self.paramsMovimiento[
                                           'jugador'],
                                       desc=self.paramsMovimiento['desc'],
                                       orden=self.paramsMovimiento['orden'])
        self.client = Client()  # Cliente web

    @classmethod
    def decode(cls, txt):
        """
        Decodifica el texto a formato UTF-8
        -----------------------------------
            :param
                txt = cadena a decodificar
        """
        return txt.decode("utf-8")

    def validate_response(self, service, response):
        """
        Comprueba si el contenido que se muestra al cliente es correcto
        ---------------------------------------------------------------
            :param service
                Pagina (servicio) a comprobar
            :param response
                Respuesta recibida del servidor

            :return m
                Booleano, True si es correcta la respuesta y False en caso
                contrario
        """

        definition = SERVICE_DEF[service]
        # print(definition["pattern"], self.decode(response.content))
        m = re.search(definition["pattern"], self.decode(response.content))
        self.assertTrue(m)
        return m

    def is_playerPage(self, response):
        """
        Solicita validar la respuesta del servidor
        para la pagina del jugador
        ------------------------------------------
            :param response
                Respuesta del servidor (contenido)
        """
        self.validate_response(PLAYER_PAGE, response)


class PlayerServicesTests(ServiceBaseTest):
    """Realiza los tests sobre la aplicacion web"""

    def test_01_playerPage(self):
        """Comprueba si la pagina del jugador funciona correctamente"""

        response = self.client.get(reverse(PLAYER_PAGE), follow=True)
        self.is_playerPage(response)
