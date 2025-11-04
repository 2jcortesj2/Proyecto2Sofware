from django.urls import path
from .views import ResultadoView

urlpatterns = [
    path('resultados/', ResultadoView.as_view(), name='resultado_list'),
    path('resultados/<int:id>/', ResultadoView.as_view(), name='resultado_detail'),
]