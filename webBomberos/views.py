from django.shortcuts import render, get_object_or_404
from django.views.defaults import page_not_found
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
import requests
from django.contrib import auth
from datetime import datetime

from .models import Compania
from .models import Voluntario
from .models import Companiavoluntario
from .models import Evento

#def mi_error_404(request):
#    nombre_template = '404.html'
#    return page_not_found(request, template_name=nombre_template)

def login_web(request):
    com = Compania.objects.all()           
    return render(request, 'webBomberos/login.html', {'compania':com})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        com = request.POST['compania']
        c = Compania.objects.get(nombrecompania=com)
        global pk_compania_actual
        pk_compania_actual = c.idcompania
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('index')
    else:
        return redirect('index')

def user_not_logged(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return redirect('index')

def logout(request):
    if  request.method == 'POST':
        auth_logout(request)
        return redirect('index')
    else:
        return redirect('home')

@login_required(login_url='/login_required')
def home(request):           
    return render(request, 'webBomberos/home.html')

@login_required(login_url='/login_required')
def compania_list(request):
    global pk_compania_actual
    com = Compania.objects.get(idcompania=pk_compania_actual)
    return render(request, 'webBomberos/compania_list.html', {'compania':com})


@login_required(login_url='/login_required')
def voluntarios_list(request):
    try:
        vol = []    
        global pk_compania_actual
        #vol = Voluntario.objects.all()
        c = Companiavoluntario.objects.filter(fk_companiavol=pk_compania_actual)
        for v in c:
            vl = Voluntario.objects.get(rut=v.fk_vol.rut)
            volun = Voluntario(rut=vl.rut,
                               nombre=vl.nombre,
                               fechanacimiento=vl.fechanacimiento,
                               ciudadnacimiento=vl.ciudadnacimiento,
                               gruposanguineo=vl.gruposanguineo,
                               profesion=vl.profesion,
                               fechaingreso=v.fechaingreso,
                               fechasalida=v.fechasalida,
                               serviciomilitar=vl.serviciomilitar,
                               insignia=vl.insignia,
                               cargo=vl.cargo,
                               calificacion=vl.calificacion)
            vol.append(volun)
        #return HttpResponse(fechas)
        return render(request, 'webBomberos/voluntario_list.html', {'voluntarios':vol})
    except Voluntario.DoesNotExist:
        vol = None
        return render(request, 'webBomberos/voluntario_list.html', {'voluntarios':vol})


@login_required(login_url='/login_required')
def voluntario_edit(request, pk):
     global pk_compania_actual
     vl = get_object_or_404(Voluntario, pk=pk)
     c = Companiavoluntario.objects.get(fk_companiavol=pk_compania_actual,fk_vol=pk)
     vol = Voluntario(rut=vl.rut,
                               nombre=vl.nombre,
                               fechanacimiento=vl.fechanacimiento,
                               ciudadnacimiento=vl.ciudadnacimiento,
                               gruposanguineo=vl.gruposanguineo,
                               profesion=vl.profesion,
                               fechaingreso=c.fechaingreso,
                               fechasalida=c.fechasalida,
                               serviciomilitar=vl.serviciomilitar,
                               insignia=vl.insignia,
                               cargo=vl.cargo,
                               calificacion=vl.calificacion)
     #return HttpResponse(vol.ciudadnacimiento)
     return render(request, 'webBomberos/voluntario_edit.html', {'voluntario':vol})

@login_required(login_url='/login_required')     
def voluntario_editado(request, pk):
    if request.method == "POST":
         global pk_compania_actual
         rut = request.POST['rut_vol']
         nombre = request.POST['nombre_vol']
         nacimiento = request.POST['nacimiento_vol']
         ciudad = request.POST['ciudad_vol']
         sangre = request.POST['sangre_vol']
         profesion = request.POST['profesion_vol']
         ingreso = request.POST['ingreso_vol']
         salida = request.POST['salida_vol']
         insignia = request.POST['insignia_vol']
         cargo = request.POST['cargo_vol']
         calificacion = request.POST['calificacion_vol']
         servicio = request.POST['servicio_vol']
         if servicio=="Si":
            ser=1
         else:
            ser=0
         global pk_compania_actual
         
         v = Voluntario.objects.get(rut=rut)
         v.rut = rut
         v.nombre = nombre
         v.fechanacimiento = nacimiento
         v.ciudadnacimiento = ciudad
         v.gruposanguineo = sangre
         v.profesion = profesion
         v.fechaingreso = ingreso
         if len(salida) == 0:
            v.fechasalida = None
            salida = None
         else:
            v.fechasalida = salida
         v.serviciomilitar = ser
         v.insignia = insignia
         v.cargo = cargo
         v.calificacion = calificacion
         #v.fk_idcompania = fk
         v.save()
         c = Companiavoluntario.objects.get(fk_companiavol=pk_compania_actual,fk_vol=rut)
         c.fechaingreso = ingreso
         c.fechasalida = salida
         c.save()
         return redirect('voluntario')
    else:
         return redirect('voluntario')


@login_required(login_url='/login_required')
def voluntario_new(request):
    return render(request, 'webBomberos/voluntario_new.html')

@login_required(login_url='/login_required')
def voluntario_guardar(request):
     if request.method == "POST":
         rut = request.POST['rut_vol']
         nombre = request.POST['nombre_vol']
         nacimiento = request.POST['nacimiento_vol']
         ciudad = request.POST['ciudad_vol']
         sangre = request.POST['sangre_vol']
         profesion = request.POST['profesion_vol']
         ingreso = request.POST['ingreso_vol']
         salida = None
         servicio = request.POST['servicio_vol']
         insignia = request.POST['insignia_vol']
         cargo = request.POST['cargo_vol']
         calificacion = request.POST['calificacion_vol']
         if servicio=="Si":
            ser=1
         else:
            ser=0
         global pk_compania_actual
         v = Voluntario(rut=rut,
                        nombre=nombre,
                        fechanacimiento=nacimiento,
                        ciudadnacimiento=ciudad,
                        gruposanguineo=sangre,
                        profesion=profesion,
                        fechaingreso=ingreso,
                        fechasalida=salida,
                        serviciomilitar=ser,
                        insignia=insignia,
                        cargo=cargo,
                        calificacion=calificacion,
                        )
         v.save()
         c = Companiavoluntario(fk_companiavol_id=pk_compania_actual,
                                fk_vol_id=rut,
                                fechaingreso=ingreso,
                                fechasalida=salida
                                )
         c.save()
         return redirect('voluntario')
     else:
        return render(request, 'webBomberos/voluntario_new.html')

@login_required(login_url='/login_required')
def informe1_list(request):
    global pk_compania_actual
    inf1 = Evento.objects.filter(fk_idcompaniae=pk_compania_actual)
    #return HttpResponse(inf1)
    return render(request, 'webBomberos/informe1_list.html', {'informe1':inf1})

@login_required(login_url='/login_required')
def informe1_edit(request,pk):
    return HttpResponse("Hola")



