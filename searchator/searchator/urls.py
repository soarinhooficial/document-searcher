
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from .views import extrair_texto_view

urlpatterns = [
    path('extrair-texto/', extrair_texto_view, name='extrair_texto'),
    # Outras rotas do seu aplicativo...
]
