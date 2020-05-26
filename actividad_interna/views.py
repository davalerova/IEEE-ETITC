from django.shortcuts import render
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