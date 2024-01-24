from django.views.generic.edit import CreateView

from .models import Tipo, Cidade, Uf, Cachaca

from django.urls import reverse_lazy

class TipoCreate(CreateView):
    model = Tipo
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Tipo de Bebida"}
    success_url = reverse_lazy("inicio")

class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Cidade"}
    success_url = reverse_lazy("inicio")

class UfCreate(CreateView):
    model = Uf
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Estado"}
    success_url = reverse_lazy("inicio")

class CachacaCreate(CreateView):
    model = Cachaca
    fields = ["nome", "tipo", "marca", "ano", "cidade", "uf", "teor", "observacoes"]
    extra_context = {"titulo": "Cadastro de Bebida"}
    template_name = "cadastros/form-cadastro.html"
    success_url = reverse_lazy("inicio")
