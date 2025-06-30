from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo_paciente/', views.nuevo_paciente, name='/nuevo_paciente/'),
    path('nuevo_medico/', views.nuevo_medico, name='/nuevo_medico/'),
    path('nuevo_turno/', views.nuevo_turno, name='/nuevo_turno/'),
    path('buscar/', views.buscar_turno, name='/buscar_turno/'),
]
