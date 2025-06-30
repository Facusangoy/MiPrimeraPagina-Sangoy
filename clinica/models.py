from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"El paciente: {self.paciente} tiene un turno con: {self.medico} el {self.fecha} a las {self.hora}"
