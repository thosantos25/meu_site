# meu_site/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagina_inicial.urls')),  # Incluindo as URLs da app
]