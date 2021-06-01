"""
Federico Pérez Fernández
04-06-2021
PSI - Conv. Extraordinaria
"""
import csv, os, django
from django.core.management.base import BaseCommand
from aplicacion.models import (Jugador, Partida, Movimiento)


class Command(BaseCommand):
    """
    This class will populate the django's app database (models).
    To execute it just type down python manage.py populate <option>.

    Check out the README for more information.
    """

    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    def add_arguments(self, parser):
        """Set the available arguments for the populate command"""
        parser.add_argument('model', type=str, help="""
        model to  update:
        all -> all models
        jugador -> players' models
        partida -> matches' models
        movimiento -> movements' models
        """)

    def handle(self, *args, **kwargs):
        """Checks out the arguments and calls to the indicated method"""
        model = kwargs['model']
        # clean database
        if model == 'all' or model == 'clean':
            self.cleanDataBase()
        if model == 'jugador' or model == 'all':
            self.jugador()
        if model == 'partida' or model == 'all':
            self.partida()
        if model == 'movimiento' or model == 'all':
            self.movimiento()

        return

    def cleanDataBase(self):
        """Cleans the database"""
        Jugador.objects.all().delete()
        Partida.objects.all().delete()
        Movimiento.objects.all().delete()

        return

    def jugador(self):
        """Creates the players and add them to the database"""

        # Diccionario con los datos de jugadores
        jugadores = [
            {'id': 1001,
             'nombreJ': 'jugador_01',
             },
            {'id': 1002,
             'nombreJ': 'jugador_02',
             },
            {'id': 1003,
             'nombreJ': 'jugador_03',
             },
        ]

        print('###### Poblando base de datos con jugadores...\n')

        for j in jugadores:
            jugador = Jugador.objects.get_or_create(id=j['id'],
                                                    nombreJ=j['nombreJ'])[0]
            jugador.save()

        print('###### Listo!\n')

        return

    def partida(self):
        """Creates the matches and add them to the database"""

        # Diccionario con los datos de partidas
        partidas = [
            {'id': 1001,
             'fecha': '2021-01-05',
             'jugadorB': 1001,
             'jugadorN': 1002
             },
            {'id': 1002,
             'fecha': '2021-01-10',
             'jugadorB': 1002,
             'jugadorN': 1003
             },
            {'id': 1003,
             'fecha': '2021-01-12',
             'jugadorB': 1003,
             'jugadorN': 1001
             },
            {'id': 1004,
             'fecha': '2021-01-15',
             'jugadorB': 1002,
             'jugadorN': 1003
             },
        ]

        print('###### Poblando base de datos con partidas...\n')

        for p in partidas:
            jugadorB = Jugador.objects.filter(id=p['jugadorB']).first()
            jugadorN = Jugador.objects.filter(id=p['jugadorN']).first()
            partida = Partida.objects.get_or_create(id=p['id'],
                                                    fecha=p['fecha'],
                                                    jugadorB=jugadorB,
                                                    jugadorN=jugadorN)[0]
            partida.save()

        print('###### Listo!\n')

        return

    def movimiento(self):
        """Creates the movements and add them to the database"""

        # Diccionario con los datos de los movimientos de una partida
        movimientos = [
            {'id': 1001,
             'partida': 1001,
             'jugador': 1001,
             'descripcion': 'e4',
             'orden': 1,
             },
            {'id': 1002,
             'partida': 1001,
             'jugador': 1002,
             'descripcion': 'e5',
             'orden': 2,
             },
            {'id': 1003,
             'partida': 1001,
             'jugador': 1001,
             'descripcion': 'Ac4',
             'orden': 3,
             },
            {'id': 1004,
             'partida': 1001,
             'jugador': 1002,
             'descripcion': 'Cc6',
             'orden': 4,
             },
        ]

        print('###### Poblando base de datos con movimientos...\n')

        for m in movimientos:
            jugador = Jugador.objects.filter(id=m['jugador']).first()
            partida = Partida.objects.filter(id=m['partida']).first()
            movimiento = Movimiento.objects.get_or_create(id=m['id'],
                                                          partida=partida,
                                                          jugador=jugador,
                                                          descripcion=m[
                                                              'descripcion'],
                                                          orden=m['orden'])[0]
            movimiento.save()

        print('###### Listo!\n')

        return
