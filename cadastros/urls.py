from django.urls import path

from .views import TipoCreate, CidadeCreate, UfCreate, CachacaCreate, TipoUpdate, CidadeUpdate, UfUpdate,  CachacaUpdate, TipoDelete, CidadeDelete, UfDelete, CachacaDelete, TipoList, CidadeList, UfList, CachacaList, TipoDetail, CidadeDetail, UfDetail, CachacaDetail

#Exemplo de url
urlpatterns = [
    #path('endereco', MinhaView.as_view(), name='nome-da-url'),

    path('cadastrar/tipo/', TipoCreate.as_view(), name="cadastrar-tipo"),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/uf/', UfCreate.as_view(), name="cadastrar-uf"),
    path('cadastrar/cachaca/', CachacaCreate.as_view(), name="cadastrar-cachaca"),

    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name="editar-tipo"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('editar/uf/<int:pk>/', UfUpdate.as_view(), name="editar-uf"),
    path('editar/cachaca/<int:pk>/', CachacaUpdate.as_view(), name="editar-cachaca"),

    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name="excluir-tipo"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('excluir/uf/<int:pk>/', UfDelete.as_view(), name="excluir-uf"),
    path('excluir/cachaca/<int:pk>/', CachacaDelete.as_view(), name="excluir-cachaca"),

    path('listar/tipo/', TipoList.as_view(), name="listar-tipo"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidade"),
    path('listar/uf/', UfList.as_view(), name="listar-uf"),
    path('listar/cachaca/', CachacaList.as_view(), name="listar-cachaca"),

    path('detalhar/tipo/', TipoDetail.as_view(), name="detalhar-tipo"),
    path('detalhar/cidade/', CidadeDetail.as_view(), name="detalhar-cidade"),
    path('detalhar/uf/', UfDetail.as_view(), name="detalhar-uf"),
    path('detalhar/cachaca/', CachacaDetail.as_view(), name="detalhar-cachaca"),


]