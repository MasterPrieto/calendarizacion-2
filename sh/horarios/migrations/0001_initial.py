# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aula'
        db.create_table(u'horarios_aula', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')()),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagen_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('proyector', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('internet', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'horarios', ['Aula'])

        # Adding model 'Profesor'
        db.create_table(u'horarios_profesor', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('instituto', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('grado', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'horarios', ['Profesor'])

        # Adding model 'Profesordiscapacidad'
        db.create_table(u'horarios_profesordiscapacidad', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('profesor_id', self.gf('django.db.models.fields.IntegerField')()),
            ('discapacidad_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Profesordiscapacidad'])

        # Adding model 'Grupo'
        db.create_table(u'horarios_grupo', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alumnos', self.gf('django.db.models.fields.IntegerField')()),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('semestre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'horarios', ['Grupo'])

        # Adding model 'Grupodiscapacidad'
        db.create_table(u'horarios_grupodiscapacidad', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('grupo_id', self.gf('django.db.models.fields.IntegerField')()),
            ('discapacidad_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Grupodiscapacidad'])

        # Adding model 'Carrera'
        db.create_table(u'horarios_carrera', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('instituto_id', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('imagen_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Carrera'])

        # Adding model 'Discapacidad'
        db.create_table(u'horarios_discapacidad', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('imagen_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Discapacidad'])

        # Adding model 'Espacio'
        db.create_table(u'horarios_espacio', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoespacio_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Espacio'])

        # Adding model 'Espaciodiscapacidad'
        db.create_table(u'horarios_espaciodiscapacidad', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('espacio_id', self.gf('django.db.models.fields.IntegerField')()),
            ('discapacidad_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Espaciodiscapacidad'])

        # Adding model 'Espaciorecurso'
        db.create_table(u'horarios_espaciorecurso', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('espacio_id', self.gf('django.db.models.fields.IntegerField')()),
            ('recurso_id', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Espaciorecurso'])

        # Adding model 'Esquema'
        db.create_table(u'horarios_esquema', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('entidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('esquema', self.gf('django.db.models.fields.TextField')()),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Esquema'])

        # Adding model 'Horariolaboral'
        db.create_table(u'horarios_horariolaboral', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('horas', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'horarios', ['Horariolaboral'])

        # Adding model 'Imagen'
        db.create_table(u'horarios_imagen', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('archivo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mime', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ancho', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('alto', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('alt', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'horarios', ['Imagen'])

        # Adding model 'Instituto'
        db.create_table(u'horarios_instituto', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'horarios', ['Instituto'])

        # Adding model 'Asignatura'
        db.create_table(u'horarios_asignatura', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('semestre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'horarios', ['Asignatura'])

        # Adding model 'Asignaturarecurso'
        db.create_table(u'horarios_asignaturarecurso', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('materia_id', self.gf('django.db.models.fields.IntegerField')()),
            ('recurso_id', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Asignaturarecurso'])

        # Adding model 'Recurso'
        db.create_table(u'horarios_recurso', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('imagen_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'horarios', ['Recurso'])

        # Adding model 'Tipoespacio'
        db.create_table(u'horarios_tipoespacio', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('imagen_id', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'horarios', ['Tipoespacio'])


    def backwards(self, orm):
        # Deleting model 'Aula'
        db.delete_table(u'horarios_aula')

        # Deleting model 'Profesor'
        db.delete_table(u'horarios_profesor')

        # Deleting model 'Profesordiscapacidad'
        db.delete_table(u'horarios_profesordiscapacidad')

        # Deleting model 'Grupo'
        db.delete_table(u'horarios_grupo')

        # Deleting model 'Grupodiscapacidad'
        db.delete_table(u'horarios_grupodiscapacidad')

        # Deleting model 'Carrera'
        db.delete_table(u'horarios_carrera')

        # Deleting model 'Discapacidad'
        db.delete_table(u'horarios_discapacidad')

        # Deleting model 'Espacio'
        db.delete_table(u'horarios_espacio')

        # Deleting model 'Espaciodiscapacidad'
        db.delete_table(u'horarios_espaciodiscapacidad')

        # Deleting model 'Espaciorecurso'
        db.delete_table(u'horarios_espaciorecurso')

        # Deleting model 'Esquema'
        db.delete_table(u'horarios_esquema')

        # Deleting model 'Horariolaboral'
        db.delete_table(u'horarios_horariolaboral')

        # Deleting model 'Imagen'
        db.delete_table(u'horarios_imagen')

        # Deleting model 'Instituto'
        db.delete_table(u'horarios_instituto')

        # Deleting model 'Asignatura'
        db.delete_table(u'horarios_asignatura')

        # Deleting model 'Asignaturarecurso'
        db.delete_table(u'horarios_asignaturarecurso')

        # Deleting model 'Recurso'
        db.delete_table(u'horarios_recurso')

        # Deleting model 'Tipoespacio'
        db.delete_table(u'horarios_tipoespacio')


    models = {
        u'horarios.asignatura': {
            'Meta': {'object_name': 'Asignatura'},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.asignaturarecurso': {
            'Meta': {'object_name': 'Asignaturarecurso'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'materia_id': ('django.db.models.fields.IntegerField', [], {}),
            'recurso_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.aula': {
            'Meta': {'object_name': 'Aula'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'internet': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'proyector': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'horarios.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {}),
            'instituto_id': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.discapacidad': {
            'Meta': {'object_name': 'Discapacidad'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'horarios.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tipoespacio_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.espaciodiscapacidad': {
            'Meta': {'object_name': 'Espaciodiscapacidad'},
            'discapacidad_id': ('django.db.models.fields.IntegerField', [], {}),
            'espacio_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'horarios.espaciorecurso': {
            'Meta': {'object_name': 'Espaciorecurso'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'espacio_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'recurso_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.esquema': {
            'Meta': {'object_name': 'Esquema'},
            'entidad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'esquema': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'alumnos': ('django.db.models.fields.IntegerField', [], {}),
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.grupodiscapacidad': {
            'Meta': {'object_name': 'Grupodiscapacidad'},
            'discapacidad_id': ('django.db.models.fields.IntegerField', [], {}),
            'grupo_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'horarios.horariolaboral': {
            'Meta': {'object_name': 'Horariolaboral'},
            'horas': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'horarios.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'alt': ('django.db.models.fields.TextField', [], {}),
            'alto': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'archivo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'mime': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'horarios.instituto': {
            'Meta': {'object_name': 'Instituto'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'horarios.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'grado': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'instituto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.profesordiscapacidad': {
            'Meta': {'object_name': 'Profesordiscapacidad'},
            'discapacidad_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'profesor_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.tipoespacio': {
            'Meta': {'object_name': 'Tipoespacio'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['horarios']