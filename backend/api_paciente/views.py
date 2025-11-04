from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Paciente
import json

class PacienteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, paciente_id=None):
        if paciente_id:
            try:
                paciente = Paciente.objects.get(paciente_id=paciente_id)
                datos = {
                    'Message': 'Success',
                    'Paciente': {
                        'paciente_id': paciente.paciente_id,
                        'codigo_ingreso': paciente.codigo_ingreso,
                        'nombre': paciente.nombre,
                        'apellidos': paciente.apellidos,
                        'direccion': paciente.direccion,
                        'telefono': paciente.telefono,
                        'insurance': paciente.insurance,
                        'fecha_registro': str(paciente.fecha_registro)
                    }
                }
            except Paciente.DoesNotExist:
                datos = {'Message': 'Paciente not found'}
            return JsonResponse(datos)
        else:
            pacientes = list(Paciente.objects.values())
            if len(pacientes) > 0:
                datos = {'Message': 'Success', 'Pacientes': pacientes}
            else:
                datos = {'Message': 'No Pacientes found'}
            return JsonResponse(datos)
    
    def post(self, request):
        JsonData = json.loads(request.body)
        Paciente.objects.create(
            paciente_id=JsonData['paciente_id'],
            codigo_ingreso=JsonData['codigo_ingreso'],
            nombre=JsonData['nombre'],
            apellidos=JsonData['apellidos'],
            direccion=JsonData['direccion'],
            telefono=JsonData['telefono'],
            insurance=JsonData['insurance'],
            fecha_registro=JsonData['fecha_registro']
        )
        datos = {'Message': 'Paciente Created Successfully'}
        return JsonResponse(datos)
    
    def put(self, request, paciente_id):
        JsonData = json.loads(request.body)
        try:
            paciente = Paciente.objects.get(paciente_id=paciente_id)
            paciente.codigo_ingreso = JsonData['codigo_ingreso']
            paciente.nombre = JsonData['nombre']
            paciente.apellidos = JsonData['apellidos']
            paciente.direccion = JsonData['direccion']
            paciente.telefono = JsonData['telefono']
            paciente.insurance = JsonData['insurance']
            paciente.fecha_registro = JsonData['fecha_registro']
            paciente.save()
            datos = {'Message': 'Paciente Updated Successfully'}
        except Paciente.DoesNotExist:
            datos = {'Message': 'Paciente not found'}
        return JsonResponse(datos)
    
    def delete(self, request, paciente_id):
        try:
            paciente = Paciente.objects.get(paciente_id=paciente_id)
            paciente.delete()
            datos = {'Message': 'Paciente Deleted Successfully'}
        except Paciente.DoesNotExist:
            datos = {'Message': 'Paciente not found'}
        return JsonResponse(datos)