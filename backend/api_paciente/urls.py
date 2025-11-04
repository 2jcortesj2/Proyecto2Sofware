from django.urls import path
from .views import PacienteView

urlpatterns = [
    path('pacientes/', PacienteView.as_view(), name='paciente_list'),
    path('pacientes/<str:paciente_id>/', PacienteView.as_view(), name='paciente_detail'),
]