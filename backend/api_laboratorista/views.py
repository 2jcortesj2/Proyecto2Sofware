from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratorista
import json

class LaboratoristaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=None):
        if id:
            try:
                laboratorista = Laboratorista.objects.get(id=id)
                datos = {
                    'Message': 'Success',
                    'Laboratorista': {
                        'id': laboratorista.id,
                        'codigo_interno': laboratorista.codigo_interno,
                        'nombre': laboratorista.nombre,
                        'titulo': laboratorista.titulo,
                        'telefono': laboratorista.telefono,
                        'email': laboratorista.email,
                        'especialidad': laboratorista.especialidad
                    }
                }
            except Laboratorista.DoesNotExist:
                datos = {'Message': 'Laboratorista not found'}
            return JsonResponse(datos)
        else:
            laboratoristas = list(Laboratorista.objects.values())
            if len(laboratoristas) > 0:
                datos = {'Message': 'Success', 'Laboratoristas': laboratoristas}
            else:
                datos = {'Message': 'No Laboratoristas found'}
            return JsonResponse(datos)
    
    def post(self, request):
        JsonData = json.loads(request.body)
        Laboratorista.objects.create(
            codigo_interno=JsonData['codigo_interno'],
            nombre=JsonData['nombre'],
            titulo=JsonData['titulo'],
            telefono=JsonData['telefono'],
            email=JsonData['email'],
            especialidad=JsonData['especialidad']
        )
        datos = {'Message': 'Laboratorista Created Successfully'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        JsonData = json.loads(request.body)
        try:
            laboratorista = Laboratorista.objects.get(id=id)
            laboratorista.codigo_interno = JsonData['codigo_interno']
            laboratorista.nombre = JsonData['nombre']
            laboratorista.titulo = JsonData['titulo']
            laboratorista.telefono = JsonData['telefono']
            laboratorista.email = JsonData['email']
            laboratorista.especialidad = JsonData['especialidad']
            laboratorista.save()
            datos = {'Message': 'Laboratorista Updated Successfully'}
        except Laboratorista.DoesNotExist:
            datos = {'Message': 'Laboratorista not found'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        try:
            laboratorista = Laboratorista.objects.get(id=id)
            laboratorista.delete()
            datos = {'Message': 'Laboratorista Deleted Successfully'}
        except Laboratorista.DoesNotExist:
            datos = {'Message': 'Laboratorista not found'}
        return JsonResponse(datos)