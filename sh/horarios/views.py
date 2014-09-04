from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aula
from .models import Profesor
from .models import Grupo
from .models import Asignatura
from .models import Carrera
from .models import Instituto
from .models import Discapacidad
from .models import Recurso
from .models import Espacio
from .models import Espaciorecurso
from .models import Tipoespacio
from .models import Asignaturarecurso
from .models import Horariolaboral
from .models import Profesordiscapacidad
from .models import Grupodiscapacidad
from .models import Espaciodiscapacidad




# Create your views here.

def index(request):
    return render(request, 'horarios/ws/index.html')

def registrocarrera(request):
    if request.method == 'POST':
        nueva_carrera = Carrera()
        nueva_carrera.tipo=request.POST['tipo']
        nueva_carrera.nombre=request.POST['nombre']
        nueva_carrera.instituto_id=request.POST['instituto_id']
        nueva_carrera.save()
        return HttpResponseRedirect('/registrocarrera')

    return render(request, 'horarios/ws/registrocarrera.html')

def registrodiscapacidad(request):
    if request.method == 'POST':
        nueva_discapacidad = Discapacidad()
        nueva_discapacidad.nombre=request.POST['nombre']
        nueva_discapacidad.descripcion=request.POST['descripcion']
        nueva_discapacidad.save()
        return HttpResponseRedirect('/registrodiscapacidad')

    return render(request, 'horarios/ws/registrodiscapacidad.html')

def registrorecurso(request):
    if request.method == 'POST':
        nueva_recurso = Recurso()
        nueva_recurso.nombre=request.POST['nombre']
        nueva_recurso.descripcion=request.POST['tipo']
        nueva_recurso.capacidad=request.POST['capacidad']
        nueva_recurso.save()
        return HttpResponseRedirect('/registrorecurso')

    return render(request, 'horarios/ws/registrorecurso.html')

def registroespacio(request):
    if request.method == 'POST':
        nueva_espacio = Espacio()
        nueva_espacio.nombre=request.POST['nombre']
        nueva_espacio.codigo=request.POST['codigo']
        nueva_espacio.capacidad=request.POST['capacidad']
        nueva_espacio.tipo=request.POST['tipo']
        nueva_espacio.descripcion=request.POST['descripcion']
        nueva_espacio.save()
        return HttpResponseRedirect('/registroespacio')

    return render(request, 'horarios/ws/registroespacio.html')

def registroespaciodiscapacidad(request):
    if request.method == 'POST':
        nuevo_espaciodiscapacidad = Espaciodiscapacidad()
        nuevo_espaciodiscapacidad.espacio_id=request.POST['espacio_id']
        nuevo_espaciodiscapacidad.discapacidad_id=request.POST['discapacidad_id']
        nuevo_espaciodiscapacidad.save()
        return HttpResponseRedirect('/registroespaciodiscapacidad')

    return render(request, 'horarios/ws/registroespaciodiscapacidad.html')

def registrotipoespacio(request):
    if request.method == 'POST':
        nueva_tipoespacio = Tipoespacio()
        nueva_tipoespacio.nombre=request.POST['nombre']
        nueva_tipoespacio.color=request.POST['color']
        nueva_tipoespacio.save()
        return HttpResponseRedirect('/registrotipoespacio')

    return render(request, 'horarios/ws/registrotipoespacio.html')

def registroespaciorecurso(request):
    if request.method == 'POST':
        nueva_espaciorecurso = Espaciorecurso()
        nueva_espaciorecurso.espacio_id=request.POST['espacio_id']
        nueva_espaciorecurso.recurso_id=request.POST['recurso_id']
        nueva_espaciorecurso.cantidad=request.POST['cantidad']
        nueva_espaciorecurso.save()
        return HttpResponseRedirect('/registroespaciorecurso')

    return render(request, 'horarios/ws/registroespaciorecurso.html')

def registroasignaturarecurso(request):
    if request.method == 'POST':
        nueva_asignaturarecurso = Asignaturarecurso()
        nueva_asignaturarecurso.asignatura_id=request.POST['espacio_id']
        nueva_asignaturarecurso.recurso_id=request.POST['recurso_id']
        nueva_asignaturarecurso.cantidad=request.POST['cantidad']
        nueva_asignaturarecurso.save()
        return HttpResponseRedirect('/registroasignaturarecurso')

    return render(request, 'horarios/ws/registroasignaturarecurso.html')

def registroinstituto(request):
    if request.method == 'POST':
        nueva_instituto = Instituto()
        nueva_instituto.nombre=request.POST['nombre']
        nueva_instituto.color=request.POST['color']
        nueva_instituto.save()
        return HttpResponseRedirect('/registroinstituto')

    return render(request, 'horarios/ws/registroinstituto.html')

def registrohorariolaboral(request):
    if request.method == 'POST':
        nueva_horariolaboral = Horariolaboral()
        nueva_horariolaboral.nombre=request.POST['nombre']
        nueva_horariolaboral.color=request.POST['color']
        nueva_horariolaboral.save()
        return HttpResponseRedirect('/registrohorariolaboral')

    return render(request, 'horarios/ws/registrohorariolaboral.html')

def registroaula(request):
    if request.method == 'POST':
        nueva_aula = Aula()
        nueva_aula.nombre=request.POST['nombre']
        nueva_aula.codigo=request.POST['codigo']
        nueva_aula.capacidad=request.POST['capacidad']
        nueva_aula.tipo=request.POST['tipo']
        nueva_aula.comentario=request.POST['comentario']

        try:
            nueva_aula.proyector=request.POST['proyector']
        except:
            nueva_aula.proyector=False
        try:
            nueva_aula.internet=request.POST['internet']
        except:
            nueva_aula.internet=False

        nueva_aula.save()
        return HttpResponseRedirect('/registroaula')

    return render(request, 'horarios/ws/registroaula.html')

def edicionaula(request,registroseleccionado):
    consulta_registro_aula= Aula.objects.get(id=registroseleccionado)

    if request.method == 'POST':
        aula = Aula.objects.select_for_update().filter(id=registroseleccionado)

        try:
            aula.update(
            nombre=request.POST['nombre'],
            codigo=request.POST['codigo'],
            capacidad=request.POST['capacidad'],
            tipo=request.POST['tipo'],
            comentario=request.POST['comentario'],
            proyector=request.POST['proyector'],
            internet=request.POST['internet'],
        )
            return render(request, 'horarios/ws/editaraula.html')

        except:

            return False

    return render(request, 'horarios/ws/edicionaula.html',{'aula':consulta_registro_aula})

def editaraula(request):
    if request.method == 'POST':
        tipo_aula=request.POST['tipo']
        consulta_aula= Aula.objects.filter(tipo=tipo_aula)
        return render(request,'horarios/ws/editaraula.html',{'consulta_aula':consulta_aula})

    return render(request, 'horarios/ws/editaraula.html')

def registroprofesor(request):
    if request.method == 'POST':
        nuevo_profesor = Profesor()
        nuevo_profesor.nombre=request.POST['nombre']
        nuevo_profesor.codigo=request.POST['codigo']
        nuevo_profesor.cargo=request.POST['cargo']
        nuevo_profesor.correo=request.POST['correo']
        nuevo_profesor.instituto=request.POST['instituto']
        nuevo_profesor.carrera=request.POST['carrera']
        nuevo_profesor.grado=request.POST['grado']
        nuevo_profesor.horaspref=request.POST['horaspref']
        try:
            nuevo_profesor.activo=request.POST['activo']
        except:
            nuevo_profesor.activo=False

        nuevo_profesor.comentario=request.POST['comentario']
        nuevo_profesor.save()
        return HttpResponseRedirect('/registroprofesor')

    return render(request, 'horarios/ws/registroprofesor.html')

def registroprofesordiscapacidad(request):
    if request.method == 'POST':
        nuevo_profesordiscapacidad = Profesordiscapacidad()
        nuevo_profesordiscapacidad.profesor_id=request.POST['profesor_id']
        nuevo_profesordiscapacidad.discapcidad_id=request.POST['discapacidad_id']
        nuevo_profesordiscapacidad.save()
        return HttpResponseRedirect('/registroprofesordiscapacidad')

    return render(request, 'horarios/ws/registroprofesordiscapacidad.html')

def edicionprofesor(request,registroseleccionado):
    consulta_registro_profesor= Profesor.objects.get(id=registroseleccionado)

    if request.method == 'POST':
        profesor = Profesor.objects.select_for_update().filter(id=registroseleccionado)

        try:
            profesor.update(
            nombre=request.POST['nombre'],
            codigo=request.POST['codigo'],
            cargo=request.POST['cargo'],
            instituto=request.POST['instituto'],
            carrera=request.POST['carrera'],
            grado=request.POST['grado'],
            comentario=request.POST['comentario'],
        )
            return render(request, 'horarios/ws/editarprofesor.html')

        except:

            return False

    return render(request, 'horarios/ws/edicionprofesor.html',{'profesor':consulta_registro_profesor})

def editarprofesor(request):
    if request.method == 'POST':
        instituto_profesor=request.POST['instituto']
        consulta_profesor= Profesor.objects.filter(instituto=instituto_profesor)

        return render(request,'horarios/ws/editarprofesor.html',{'consulta_profesor':consulta_profesor})

    return render(request, 'horarios/ws/editarprofesor.html')

def registroasignatura(request):
    if request.method == 'POST':
        nueva_asignatura = Asignatura()
        nueva_asignatura.nombre=request.POST['nombre']
        nueva_asignatura.codigo=request.POST['codigo']
        nueva_asignatura.carrera=request.POST['carrera']
        nueva_asignatura.semestre=request.POST['semestre']
        nueva_asignatura.lugar=request.POST['lugar']
        nueva_asignatura.comentario=request.POST['comentario']
        try:
            nueva_asignatura.deespecialidad=request.POST['deespecialidad']
        except:
            nueva_asignatura.deespecialidad=False

        nueva_asignatura.save()
        return HttpResponseRedirect('/registroasignatura')

    return render(request, 'horarios/ws/registroasignatura.html')

def edicionasignatura(request,registroseleccionado):
    consulta_registro_asignatura= Asignatura.objects.get(id=registroseleccionado)

    if request.method == 'POST':
        asignatura = Asignatura.objects.select_for_update().filter(id=registroseleccionado)

        try:
            asignatura.update(
            nombre=request.POST['nombre'],
            codigo=request.POST['codigo'],
            carrera=request.POST['carrera'],
            semestre=request.POST['semestre'],
            lugar=request.POST['lugar'],
            comentario=request.POST['comentario'],
        )
            return render(request, 'horarios/ws/editarasignatura.html')

        except:

            return False

    return render(request, 'horarios/ws/edicionasignatura.html',{'asignatura':consulta_registro_asignatura})

def editarasignatura(request):
    if request.method == 'POST':
        carrera_asignatura=request.POST['carrera']
        consulta_asignatura= Asignatura.objects.filter(carrera=carrera_asignatura)
        return render(request,'horarios/ws/editarasignatura.html',{'consulta_asignatura':consulta_asignatura})

    return render(request, 'horarios/ws/editarasignatura.html')

def registrogrupo(request):
    if request.method == 'POST':
        nuevo_grupo = Grupo()
        nuevo_grupo.nombre=request.POST['nombre']
        nuevo_grupo.codigo=request.POST['codigo']
        nuevo_grupo.alumnos=request.POST['alumnos']
        nuevo_grupo.carrera=request.POST['carrera']
        nuevo_grupo.semestre=request.POST['semestre']
        nuevo_grupo.comentario=request.POST['comentario']
        nuevo_grupo.save()
        return HttpResponseRedirect('/registrogrupo')

    return render(request, 'horarios/ws/registrogrupo.html')

def registrogrupodiscapacidad(request):
    if request.method == 'POST':
        nuevo_grupodiscapacidad = Grupodiscapacidad()
        nuevo_grupodiscapacidad.grupo_id=request.POST['grupo_id']
        nuevo_grupodiscapacidad.discapacidad_id=request.POST['discapacidad_id']
        nuevo_grupodiscapacidad.save()
        return HttpResponseRedirect('/registrogrupodiscapacidad')

    return render(request, 'horarios/ws/registrogrupodiscapacidad.html')



def editargrupo(request):
    if request.method == 'POST':
        carrera_grupo=request.POST['carrera']
        consulta_grupo= Grupo.objects.filter(carrera=carrera_grupo)
        return render(request,'horarios/ws/editargrupo.html',{'consulta_grupo':consulta_grupo})

    return render(request, 'horarios/ws/editargrupo.html')

def ediciongrupo(request,registroseleccionado):
    consulta_registro_grupo= Grupo.objects.get(id=registroseleccionado)

    if request.method == 'POST':
        grupo = Grupo.objects.select_for_update().filter(id=registroseleccionado)

        try:
            grupo.update(
            nombre=request.POST['nombre'],
            codigo=request.POST['codigo'],
            alumnos=request.POST['alumnos'],
            carrera=request.POST['carrera'],
            semestre=request.POST['semestre'],
            comentario=request.POST['comentario'],
        )
            return render(request, 'horarios/ws/editargrupo.html')

        except:

            return False

    return render(request, 'horarios/ws/ediciongrupo.html',{'grupo':consulta_registro_grupo})


def institutos(request, listainstitutos):
    institutos = Instituto.objects.filter(id=listainstitutos.nombre)
    return {'institutos': institutos}

'''if request.method == 'POST':
        nueva_aula = Aula()
        nueva_aula.nombre=request.POST['nombre']
        nueva_aula.codigo=request.POST['codigo']
        nueva_aula.capacidad=request.POST['capacidad']
        nueva_aula.tipo=request.POST['tipo']
        nueva_aula.comentario=request.POST['comentario']
        try:
            nueva_aula.proyector=request.POST['proyector']
        except:
            nueva_aula.proyector=False

        try:
            nueva_aula.internet=request.POST['internet']
        except:
            nueva_aula.internet=False

        nueva_aula.save()
        return HttpResponseRedirect('/registroaula')'''
