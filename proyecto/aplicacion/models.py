"""
Federico Pérez Fernández
04-06-2021
PSI - Conv. Extraordinaria
"""

from django.db import models
from django.utils import timezone


class Jugador(models.Model):
    """
    Clase Jugador
    ----------------
        nombreJ: nombre del jugador
    """
    nombreJ = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.nombreJ


class Partida(models.Model):
    """
    Clase Partida
    ----------------
        fecha: fecha de la partida
        jugadorB: id JugadorB
        jugadorN: id JugadorN
    """
    fecha = models.DateTimeField(default=timezone.now)
    jugadorB = models.ForeignKey(Jugador, on_delete=models.CASCADE,
                                 related_name='jugadorB')
    jugadorN = models.ForeignKey(Jugador, on_delete=models.CASCADE,
                                 related_name='jugadorN')

    def __str__(self):
        return str(self.id)


class Movimiento(models.Model):
    """
    Clase Movimiento
    ----------------
        partida: id Partida
        jugador: id Jugador
        descripcion: posicion nueva
        orden: numero de movimiento
    """
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=4)
    orden = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Movimientos'

    def __str__(self):
        return str(self.partida) + ' ' + str(self.jugador)
