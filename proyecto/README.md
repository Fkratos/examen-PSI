# PSI - Convocatoria Extraordinaria

Federico Pérez Fernández  
04-06-2021

## Comandos

Iniciar servidor

    python manage.py runserver <opcional: host:port>
    
Poblar base de datos
> all: Borra los datos previos de la base de datos y añade los nuevos  
> jugador: Borra los datos previos de los jugadores y añade los nuevos  
> partida: Borra los datos previos de las partidas y añade las nuevas  
> movimiento: Borra los datos previos de los movimientos y añade los nuevos  

    python manage.py poblar all


## Instrucciones

Crear proyecto Django

    django-admin.py startproject <nombreProyecto>
    
Crear app (dentro del proyecto)

    python manage.py startapp <nombreApp>

Crear base de datos en PostgreSQL

    dropdb -U alumnodb -h localhost <nombreDB>
    createdb -U alumnodb -h localhost <nombreDB>
    
    psql -U alumnodb <nombreDB> #Conectar a postgres por terminal
    \l #Listar bases de datos del usuario
    \c <nombreDB> #Conectar a una BD
    \q #Salir de shell postgres
    
Migrar base de datos (Despues de crear los modelos)

    python manage.py migrate
    
Crear superusuario

    python manage.py createsuperuser

Cargar migraciones en la base de datos

    python manage.py makemigrations <nombreApp>
    python manage.py migrate
    
## Test

Ejecutar test

    python manage.py test aplication.tests
    
## Heroku

    