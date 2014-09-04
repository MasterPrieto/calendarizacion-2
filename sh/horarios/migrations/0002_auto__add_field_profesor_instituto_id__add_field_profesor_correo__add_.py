# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profesor.instituto_id'
        db.add_column(u'horarios_profesor', 'instituto_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profesor.correo'
        db.add_column(u'horarios_profesor', 'correo',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'Profesor.imagen_id'
        db.add_column(u'horarios_profesor', 'imagen_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Profesor.horaspref'
        db.add_column(u'horarios_profesor', 'horaspref',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'Profesor.activo'
        db.add_column(u'horarios_profesor', 'activo',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Grupo.carrera_id'
        db.add_column(u'horarios_grupo', 'carrera_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Grupo.semestre'
        db.alter_column(u'horarios_grupo', 'semestre', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'Asignatura.carrera_id'
        db.add_column(u'horarios_asignatura', 'carrera_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Asignatura.color'
        db.add_column(u'horarios_asignatura', 'color',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=10),
                      keep_default=False)

        # Adding field 'Asignatura.imagen_id'
        db.add_column(u'horarios_asignatura', 'imagen_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Asignatura.horaspref'
        db.add_column(u'horarios_asignatura', 'horaspref',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profesor.instituto_id'
        db.delete_column(u'horarios_profesor', 'instituto_id')

        # Deleting field 'Profesor.correo'
        db.delete_column(u'horarios_profesor', 'correo')

        # Deleting field 'Profesor.imagen_id'
        db.delete_column(u'horarios_profesor', 'imagen_id')

        # Deleting field 'Profesor.horaspref'
        db.delete_column(u'horarios_profesor', 'horaspref')

        # Deleting field 'Profesor.activo'
        db.delete_column(u'horarios_profesor', 'activo')

        # Deleting field 'Grupo.carrera_id'
        db.delete_column(u'horarios_grupo', 'carrera_id')


        # Changing field 'Grupo.semestre'
        db.alter_column(u'horarios_grupo', 'semestre', self.gf('django.db.models.fields.CharField')(max_length=255))
        # Deleting field 'Asignatura.carrera_id'
        db.delete_column(u'horarios_asignatura', 'carrera_id')

        # Deleting field 'Asignatura.color'
        db.delete_column(u'horarios_asignatura', 'color')

        # Deleting field 'Asignatura.imagen_id'
        db.delete_column(u'horarios_asignatura', 'imagen_id')

        # Deleting field 'Asignatura.horaspref'
        db.delete_column(u'horarios_asignatura', 'horaspref')


    models = {
        u'horarios.asignatura': {
            'Meta': {'object_name': 'Asignatura'},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'carrera_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'comentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'horaspref': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios.asignaturarecurso': {
            'Meta': {'object_name': 'Asignaturarecurso'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'materia_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'imagen_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'horarios.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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