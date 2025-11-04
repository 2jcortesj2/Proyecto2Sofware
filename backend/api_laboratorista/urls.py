from django.urls import path
from .views import LaboratoristaView

urlpatterns = [
    path('laboratoristas/', LaboratoristaView.as_view(), name='laboratorista_list'),
    path('laboratoristas/<int:id>/', LaboratoristaView.as_view(), name='laboratorista_detail'),
]