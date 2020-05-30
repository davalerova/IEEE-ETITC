from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import Miembro
from django.contrib.auth.models import User
#from .forms import *


########################################################################################################################

class MiembroView(generic.ListView):
    model = Miembro
    template_name = 'miembro/miembro_listar.html'
    context_object_name = 'obj'




def miembro_inactivar(request, id):
    miembro = Miembro.objects.filter(pk=id).first()
    usuario = User.objects.filter(pk=miembro.usuario.id).first()
    contexto={}
    template_name="miembro/miembro_del.html"


    if not miembro:
        return redirect("miembro:miembro_listar")
    
    if request.method=='GET':
        contexto={'obj':miembro}
    
    if request.method=='POST':
        miembro.activo=False
        miembro.save()
        usuario.is_active=False
        usuario.save()
        return redirect("miembro:miembro_listar")

    return render(request,template_name,contexto)