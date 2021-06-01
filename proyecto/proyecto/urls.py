"""
Federico Pérez Fernández
DD--MM--YYYY
PSI - Conv. Extraordinaria
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings

from aplicacion import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aplicacion/', include('aplicacion.urls')),
    path('admin/', admin.site.urls),
]
