from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import Actividad_interna
#from .forms import *


########################################################################################################################

class ActividadInternaView(generic.ListView):
    model = Actividad_interna
    template_name = 'actividad_interna/actividad_listar.html'
    context_object_name = 'obj'


def actividad_inactivar(request, id):
    actividad_interna = Actividad_interna.objects.filter(pk=id).first()
    contexto={}
    template_name="actividad_interna/actividad_del.html"


    if not actividad_interna:
        return redirect("actividad_interna:actividad_listar")
    
    if request.method=='GET':
        contexto={'obj':actividad_interna}
    
    if request.method=='POST':
        actividad_interna.activo=False
        actividad_interna.save()
        return redirect("actividad_interna:actividad_listar")

    return render(request,template_name,contexto)