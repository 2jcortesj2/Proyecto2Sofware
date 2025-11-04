from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_paciente.urls')),
    path('api/', include('api_resultado.urls')),
    path('api/', include('api_laboratorista.urls')),
]