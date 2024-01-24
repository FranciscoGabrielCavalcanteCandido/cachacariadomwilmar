from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Tipo, Cidade, Uf, Cachaca

from django.urls import reverse_lazy

class TipoCreate(CreateView):
    model = Tipo
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Tipo de Bebida"}
    success_url = reverse_lazy("listar-tipo")

class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome", "uf"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Cidade de Origem"}
    success_url = reverse_lazy("listar-cidade")

class UfCreate(CreateView):
    model = Uf
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Estado de Origem"}
    success_url = reverse_lazy("listar-uf")

class CachacaCreate(CreateView):
    model = Cachaca
    fields = ["nome", "tipo", "marca", "ano", "cidade", "teor", "observacoes"]
    extra_context = {"titulo": "Cadastro de Bebida"}
    template_name = "cadastros/form-cadastro.html"
    success_url = reverse_lazy("listar-cachaca")

#========================================================================================#

class TipoUpdate(UpdateView):
    model = Tipo
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Tipos"}
    success_url = reverse_lazy("listar-tipo")

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ["nome", "uf"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Cidade de Origem"}
    success_url = reverse_lazy("listar-cidade")

class UfUpdate(UpdateView):
    model = Uf
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Estado de Origem"}
    success_url = reverse_lazy("listar-uf")

class CachacaUpdate(UpdateView):
    model = Cachaca
    fields = ["nome", "tipo", "marca", "ano", "cidade", "teor", "observacoes"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Bebidas / Cachaças"}
    success_url = reverse_lazy("listar-cachaca")

#========================================================================================#
    
class TipoDelete(DeleteView):
    model = Tipo
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-tipo")

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-cidade")

class UfDelete(DeleteView):
    model = Uf
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-uf")

class CachacaDelete(DeleteView):
    model = Cachaca
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-cachaca")

#========================================================================================#
    
class TipoList(ListView):
    model = Tipo
    template_name = "cadastros/list/tipo.html"

class CidadeList(ListView):
    model = Cidade
    template_name = "cadastros/list/cidade.html"

class UfList(ListView):
    model = Uf
    template_name = "cadastros/list/uf.html"

class CachacaList(ListView):
    model = Cachaca
    template_name = "cadastros/list/cachaca.html"

#========================================================================================#
    
class TipoDetail(DetailView):
    model = Tipo
    template_name = "cadastros/detail/marca.html"

class CidadeDetail(DetailView):
    model = Cidade
    template_name = "cadastros/detail/marca.html"

class UfDetail(DetailView):
    model = Uf
    template_name = "cadastros/detail/marca.html"

class CachacaDetail(DetailView):
    model = Cachaca
    template_name = "cadastros/detail/marca.html"