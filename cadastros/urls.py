from django.urls import path

from .views import TipoCreate, CidadeCreate, UfCreate, CachacaCreate

#Exemplo de url
urlpatterns = [
    #path('endereco', MinhaView.as_view(), name='nome-da-url'),
    path('cadastrar/tipo/', TipoCreate.as_view(), name="cadastrar-tipo"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/uf/', UfCreate.as_view(), name="cadastrar-uf"),
    path('cadastrar/cachaca/', CachacaCreate.as_view(), name="cadastrar-cachaca"),
]