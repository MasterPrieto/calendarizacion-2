# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Aula(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    codigo = models.IntegerField()
    capacidad = models.IntegerField()
    tipo = models.CharField(max_length=200)
    comentario = models.CharField(max_length=200)
    imagen_id = models.IntegerField(default=0)
    proyector=models.NullBooleanField()
    internet=models.NullBooleanField()
    '''class Meta:
        managed = False
        db_table = 'carrera'''

class Profesor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    '''apellidos = models.CharField(max_length=255)'''
    instituto_id = models.IntegerField(default=0)
    cargo = models.CharField(max_length=255)
    instituto = models.CharField(max_length=255)
    correo = models.CharField(max_length=255,default=None)
    imagen_id = models.IntegerField(default=0)
    carrera = models.CharField(max_length=255)
    grado = models.CharField(max_length=255) # TODO pasar a numerico 1 Lic/Ing 2 Maestro 3 Doctor
                                             # default 1
    comentario = models.CharField(max_length=200)
    horaspref = models.CharField(max_length=255,default=None)
    horariolaboral_id = models.IntegerField(default=0)   # Agregado Jose
    activo = models.NullBooleanField()      # 
    '''class Meta:
        managed = False
        db_table = 'profesor'''

# TODO Agregar tabla Cargo
# TODO Agregar tabla ProfesorCargo
# TODO Agregar tabla Profesorasignatura con el campo extra "preferente"


class Profesordiscapacidad(models.Model):
    id = models.IntegerField(primary_key=True)
    profesor_id = models.IntegerField(default=0)
    discapacidad_id = models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'profesordiscapacidad'''

class Grupo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50)
    alumnos = models.IntegerField()
    carrera = models.CharField(max_length=255)
    semestre = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    carrera_id = models.IntegerField(default=0)
    semestre = models.IntegerField()
    '''class Meta:
        managed = False
        db_table = 'grupo'''


class Grupodiscapacidad(models.Model):
    id = models.IntegerField(primary_key=True)
    grupo_id = models.IntegerField(default=0)
    discapacidad_id = models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'grupodiscapacidad'''

class Carrera(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.IntegerField()
    nombre = models.CharField(unique=True, max_length=100)
    instituto_id = models.IntegerField(default=0)
    color = models.CharField(max_length=10)
    imagen_id = models.IntegerField()
    '''class Meta:
        managed = False
        db_table = 'carrera'''

class Discapacidad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    comentario = models.CharField(max_length=255)
    imagen_id = models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'discapacidad'''

class Espacio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)
    codigo = models.CharField(max_length=20)
    comentario = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    tipoespacio_id = models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'espacio'''

class Espaciodiscapacidad(models.Model):
    id = models.IntegerField(primary_key=True)
    espacio_id = models.IntegerField(default=0)
    discapacidad_id = models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'espaciodiscapacidad'''


class Espaciorecurso(models.Model):
    id = models.IntegerField(primary_key=True)
    espacio_id = models.IntegerField(default=0)
    recurso_id = models.IntegerField(default=0)
    cantidad = models.IntegerField()
    '''class Meta:
        managed = False
        db_table = 'espaciorecurso'''

class Esquema(models.Model):
    id = models.IntegerField(primary_key=True)
    entidad = models.CharField(max_length=100)
    esquema = models.TextField()
    version = models.IntegerField()
    '''class Meta:
        managed = False
        db_table = 'esquema'''



class Horariolaboral(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.IntegerField(unique=True)
    horas = models.CharField(max_length=255)
    '''class Meta:
        managed = False
        db_table = 'horariolaboral'''

class Imagen(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)
    archivo = models.CharField(max_length=255)
    mime = models.CharField(max_length=255)
    ancho = models.CharField(max_length=10)
    alto = models.CharField(max_length=10)
    alt = models.TextField()
    '''class Meta:
        managed = False
        db_table = 'imagen'''

class Instituto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)
    color = models.CharField(max_length=10)
    '''class Meta:
        managed = False
        db_table = 'instituto'''

class Asignatura(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=20)    # Etiqueta: Numero de Trabajaador
    nombre = models.CharField(max_length=255)
    carrera=models.CharField(max_length=255)
    semestre=models.CharField(max_length=255)  # TODO pasar a numerico
    lugar=models.CharField(max_length=255)
    comentario = models.CharField(max_length=200)
    carrera_id = models.IntegerField(default=0)
    color = models.CharField(max_length=10)
    imagen_id = models.IntegerField(default=0)
    horaspref = models.CharField(max_length=255)
    deespecialidad=models.NullBooleanField()

    '''class Meta:
        managed = False
        db_table = 'asignatura'''

class Asignaturarecursada(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id=models.IntegerField(default=0)
    asignatura_id=models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'asignaturarecursada'''

class Asignaturarecurso(models.Model):
    id = models.IntegerField(primary_key=True)
    asignatura_id = models.IntegerField(default=0)
    recurso_id = models.IntegerField(default=0)
    cantidad = models.IntegerField()
    '''class Meta:
        managed = False
        db_table = 'asignaturarecurso'''

class Asignacion(models.Model):
    id = models.IntegerField(primary_key=True)
    anio=models.CharField(max_length=255)
    periodo=models.CharField(max_length=255)
    profesor_id=models.IntegerField(default=0)
    asignatura_id=models.IntegerField(default=0)
    comentario=models.CharField(max_length=255)
    '''class Meta:
        managed = False
        db_table = 'asignacion'''

# TODO FUTURO: Agregar tabla Asignacionrecurso como tabla relacional Asingacion *-* Recurso

class Periodo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=255)
    '''class Meta:
        managed = False
        db_table = 'asignaturarecursada'''

class Recurso(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    tipo = models.IntegerField()
    capacidad = models.IntegerField()
    imagen_id = models.IntegerField(default=0)
    '''class Meta:
        managed = False
        db_table = 'recurso'''

class Tipoespacio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)
    imagen_id = models.IntegerField(default=0)
    color = models.CharField(max_length=10)
    '''class Meta:
        managed = False
        db_table = 'tipoespacio'''

