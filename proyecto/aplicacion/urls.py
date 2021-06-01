"""
Federico Pérez Fernández
DD--MM--YYYY
PSI - Conv. Extraordinaria
"""

from django.urls import path
from aplicacion import views

app_name = 'aplicacion'

urlpatterns = [
    path('', views.index, name='index'),
    path('jugador/', views.jugador, name='jugador'),
]
