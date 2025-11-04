from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import ResultadoPerfilLipidico
from api_paciente.models import Paciente
from api_laboratorista.models import Laboratorista
import json

class ResultadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=None):
        if id:
            try:
                resultado = ResultadoPerfilLipidico.objects.get(id=id)
                datos = {
                    'Message': 'Success',
                    'Resultado': {
                        'id': resultado.id,
                        'paciente_id': resultado.paciente.paciente_id,
                        'laboratorista_id': resultado.laboratorista.id,
                        'colesterol_total': resultado.colesterol_total,
                        'colesterol_hdl': resultado.colesterol_hdl,
                        'colesterol_ldl': resultado.colesterol_ldl,
                        'trigliceridos': resultado.trigliceridos,
                        'fecha_analisis': str(resultado.fecha_analisis),
                        'observaciones': resultado.observaciones
                    }
                }
            except ResultadoPerfilLipidico.DoesNotExist:
                datos = {'Message': 'Resultado not found'}
            return JsonResponse(datos)
        else:
            resultados = ResultadoPerfilLipidico.objects.all()
            resultados_list = []
            for resultado in resultados:
                resultados_list.append({
                    'id': resultado.id,
                    'paciente_id': resultado.paciente.paciente_id,
                    'laboratorista_id': resultado.laboratorista.id,
                    'colesterol_total': resultado.colesterol_total,
                    'colesterol_hdl': resultado.colesterol_hdl,
                    'colesterol_ldl': resultado.colesterol_ldl,
                    'trigliceridos': resultado.trigliceridos,
                    'fecha_analisis': str(resultado.fecha_analisis),
                    'observaciones': resultado.observaciones
                })
            if len(resultados_list) > 0:
                datos = {'Message': 'Success', 'Resultados': resultados_list}
            else:
                datos = {'Message': 'No Resultados found'}
            return JsonResponse(datos)
    
    def post(self, request):
        JsonData = json.loads(request.body)
        try:
            paciente = Paciente.objects.get(paciente_id=JsonData['paciente_id'])
            laboratorista = Laboratorista.objects.get(id=JsonData['laboratorista_id'])
            
            ResultadoPerfilLipidico.objects.create(
                paciente=paciente,
                laboratorista=laboratorista,
                colesterol_total=JsonData['colesterol_total'],
                colesterol_hdl=JsonData['colesterol_hdl'],
                colesterol_ldl=JsonData['colesterol_ldl'],
                trigliceridos=JsonData['trigliceridos'],
                fecha_analisis=JsonData['fecha_analisis'],
                observaciones=JsonData['observaciones']
            )
            datos = {'Message': 'Resultado Created Successfully'}
        except Paciente.DoesNotExist:
            datos = {'Message': 'Paciente not found'}
        except Laboratorista.DoesNotExist:
            datos = {'Message': 'Laboratorista not found'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        JsonData = json.loads(request.body)
        try:
            resultado = ResultadoPerfilLipidico.objects.get(id=id)
            paciente = Paciente.objects.get(paciente_id=JsonData['paciente_id'])
            laboratorista = Laboratorista.objects.get(id=JsonData['laboratorista_id'])
            
            resultado.paciente = paciente
            resultado.laboratorista = laboratorista
            resultado.colesterol_total = JsonData['colesterol_total']
            resultado.colesterol_hdl = JsonData['colesterol_hdl']
            resultado.colesterol_ldl = JsonData['colesterol_ldl']
            resultado.trigliceridos = JsonData['trigliceridos']
            resultado.fecha_analisis = JsonData['fecha_analisis']
            resultado.observaciones = JsonData['observaciones']
            resultado.save()
            datos = {'Message': 'Resultado Updated Successfully'}
        except ResultadoPerfilLipidico.DoesNotExist:
            datos = {'Message': 'Resultado not found'}
        except Paciente.DoesNotExist:
            datos = {'Message': 'Paciente not found'}
        except Laboratorista.DoesNotExist:
            datos = {'Message': 'Laboratorista not found'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        try:
            resultado = ResultadoPerfilLipidico.objects.get(id=id)
            resultado.delete()
            datos = {'Message': 'Resultado Deleted Successfully'}
        except ResultadoPerfilLipidico.DoesNotExist:
            datos = {'Message': 'Resultado not found'}
        return JsonResponse(datos)