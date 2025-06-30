from django.contrib import admin
from .models import Paciente, Medico, Turno

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'fecha_nacimiento')
    search_fields = ('nombre', 'dni')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad')
    search_fields = ('nombre', 'especialidad')

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'fecha', 'hora')
    list_filter = ('medico', 'fecha')
    search_fields = ('paciente__nombre', 'medico__nombre')
