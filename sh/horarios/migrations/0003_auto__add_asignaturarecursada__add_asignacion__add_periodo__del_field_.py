# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Asignaturarecursada'
        db.create_table(u'horarios_asignaturarecursada', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('group_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('asignatura_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'horarios', ['Asignaturarecursada'])

        # Adding model 'Asignacion'
        db.create_table(u'horarios_asignacion', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('anio', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('profesor_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('asignatura_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comentario', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'horarios', ['Asignacion'])

        # Adding model 'Periodo'
        db.create_table(u'horarios_periodo', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'horarios', ['Periodo'])

        # Deleting field 'Asignaturarecurso.materia_id'
        db.delete_column(u'horarios_asignaturarecurso', 'materia_id')

        # Adding field 'Asignaturarecurso.asignatura_id'
        db.add_column(u'horarios_asignaturarecurso', 'asignatura_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Discapacidad.descripcion'
        db.add_column(u'horarios_discapacidad', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Espacio.descripcion'
        db.add_column(u'horarios_espacio', 'descripcion',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'Asignatura.despecialidad'
        db.add_column(u'horarios_asignatura', 'despecialidad',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Asignaturarecursada'
        db.delete_table(u'horarios_asignaturarecursada')

        # Deleting model 'Asignacion'
        db.delete_table(u'horarios_asignacion')

        # Deleting model 'Periodo'
        db.delete_table(u'horarios_periodo')

        # Adding field 'Asignaturarecurso.materia_id'
        db.add_column(u'horarios_asignaturarecurso', 'materia_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Asignaturarecurso.asignatura_id'
        db.delete_column(u'horarios_asignaturarecurso', 'asignatura_id')

        # Deleting field 'Discapacidad.descripcion'
        db.delete_column(u'horarios_discapacidad', 'descripcion')

        # Deleting field 'Espacio.descripcion'
        db.delete_column(u'horarios_espacio', 'descripcion')

        # Deleting field 'Asignatura.despecialidad'
        db.delete_column(u'horarios_asignatura', 'despecialidad')


    models = {
        u'horarios.asignacion': {
            'Meta': {'object_name': 'Asignacion'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'asignatura_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profesor_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'horarios.asignatura': {
            'Meta': {'object_name': 'Asignatura'},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'carrera_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'despecialidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'horaspref': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.asignaturarecursada': {
            'Meta': {'object_name': 'Asignaturarecursada'},
            'asignatura_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'group_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'horarios.asignaturarecurso': {
            'Meta': {'object_name': 'Asignaturarecurso'},
            'asignatura_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'recurso_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'instituto_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.discapacidad': {
            'Meta': {'object_name': 'Discapacidad'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'horarios.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'tipoespacio_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'horarios.espaciodiscapacidad': {
            'Meta': {'object_name': 'Espaciodiscapacidad'},
            'discapacidad_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'espacio_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'horarios.espaciorecurso': {
            'Meta': {'object_name': 'Espaciorecurso'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'espacio_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'recurso_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'carrera_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.grupodiscapacidad': {
            'Meta': {'object_name': 'Grupodiscapacidad'},
            'discapacidad_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grupo_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
        u'horarios.periodo': {
            'Meta': {'object_name': 'Periodo'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'activo': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'correo': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255'}),
            'grado': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'horaspref': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'instituto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'instituto_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.profesordiscapacidad': {
            'Meta': {'object_name': 'Profesordiscapacidad'},
            'discapacidad_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'profesor_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'horarios.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'horarios.tipoespacio': {
            'Meta': {'object_name': 'Tipoespacio'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['horarios']