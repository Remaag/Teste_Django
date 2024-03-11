from django.shortcuts import render

# Create your views here.
from .models import Paciente

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/pacientes/templates/pacientes/lista_pacientes.html', {'pacientes': pacientes})
