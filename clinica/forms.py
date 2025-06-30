from django import forms
from .models import Paciente, Medico, Turno

class Paciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'ingrese su nombre'}),
            'dni': forms.TextInput(attrs={'placeholder': 'ingrese su dni'}),
            'fecha_nacimiento': forms.TextInput(attrs={'placeholder': 'dd/mm/aa'}),
        }

class Medico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'nombre del medico'}),
            'especialidad': forms.TextInput(attrs={'placeholder': 'ingrese la especialidad'}),
        }


class Turno(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.DateInput(attrs={'type': 'time'}),
        }

class BuscarTurno(forms.Form):
    nombre = forms.CharField(label='Nombre del paciente', max_length=100)
    fields = '__all__'
    widgets = {
            'buscar_nombre': forms.TextInput(attrs={'placeholder': 'ingrese su nombre'}),
        }
