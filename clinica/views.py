from django.shortcuts import render, redirect
from .models import Turno as TurnoModel, Paciente as PacienteModel, Medico as MedicoModel
from .forms import Turno as TurnoForm, Paciente as PacienteForm, Medico as MedicoForm, BuscarTurno

def inicio(request):
    turnos = TurnoModel.objects.all()
    return render(request, 'clinica/inicio.html', {'turnos': turnos})

def nuevo_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'clinica/paciente.html', {'form': form})

def nuevo_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'clinica/medico.html', {'form': form})

def nuevo_turno(request):
    form = TurnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'clinica/turno.html', {'form': form})

def buscar_turno(request):
    resultados = None
    form = BuscarTurno(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = TurnoModel.objects.filter(paciente__nombre__icontains=nombre)
    return render(request, 'clinica/buscar.html', {'form': form, 'resultados': resultados})
