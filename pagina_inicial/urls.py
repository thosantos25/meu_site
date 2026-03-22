from django.urls import path
from . import views

urlpatterns = [
    # Mudei de name='home' para name='inicio' para facilitar
    path('', views.pagina_inicial, name='inicio'),
    path('catalogo/', views.catalogo, name='destinos'), 
    path('contato/', views.descricao, name='contato'),    
]