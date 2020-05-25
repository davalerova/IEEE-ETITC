from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .models import Miembro
#from .forms import *


########################################################################################################################

class MiembroView(generic.ListView):
    model = Miembro
    template_name = 'miembro/miembro_listar.html'
    context_object_name = 'obj'
