from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Tipo, Cidade, Uf, Cachaca

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class TipoCreate(LoginRequiredMixin, CreateView):
    model = Tipo
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Tipo de Bebida"}
    success_url = reverse_lazy("listar-tipo")

class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ["nome", "uf"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Cidade de Origem"}
    success_url = reverse_lazy("listar-cidade")

class UfCreate(LoginRequiredMixin, CreateView):
    model = Uf
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Cadastro de Estado de Origem"}
    success_url = reverse_lazy("listar-uf")

class CachacaCreate(LoginRequiredMixin, CreateView):
    model = Cachaca
    fields = ["nome", "tipo", "marca", "ano", "cidade", "teor", "observacoes"]
    extra_context = {"titulo": "Cadastro de Bebida"}
    template_name = "cadastros/form-cadastro.html"
    success_url = reverse_lazy("listar-cachaca")

#========================================================================================#

class TipoUpdate(LoginRequiredMixin, UpdateView):
    model = Tipo
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Tipos"}
    success_url = reverse_lazy("listar-tipo")

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ["nome", "uf"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Cidade de Origem"}
    success_url = reverse_lazy("listar-cidade")

class UfUpdate(LoginRequiredMixin, UpdateView):
    model = Uf
    fields = ["nome"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Estado de Origem"}
    success_url = reverse_lazy("listar-uf")

class CachacaUpdate(LoginRequiredMixin, UpdateView):
    model = Cachaca
    fields = ["nome", "tipo", "marca", "ano", "cidade", "teor", "observacoes"]
    template_name = "cadastros/form-cadastro.html"
    extra_context = {"titulo": "Editar Bebidas / Cachaças"}
    success_url = reverse_lazy("listar-cachaca")

#========================================================================================#
    
class TipoDelete(LoginRequiredMixin, DeleteView):
    model = Tipo
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-tipo")

class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-cidade")

class UfDelete(LoginRequiredMixin, DeleteView):
    model = Uf
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-uf")

class CachacaDelete(LoginRequiredMixin, DeleteView):
    model = Cachaca
    template_name = "cadastros/form-delete.html"
    success_url = reverse_lazy("listar-cachaca")

#========================================================================================#
    
class TipoList(LoginRequiredMixin, ListView):
    model = Tipo
    template_name = "cadastros/list/tipo.html"

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = "cadastros/list/cidade.html"

class UfList(LoginRequiredMixin, ListView):
    model = Uf
    template_name = "cadastros/list/uf.html"

class CachacaList(LoginRequiredMixin, ListView):
    model = Cachaca
    template_name = "cadastros/list/cachaca.html"

#========================================================================================#
    
class TipoDetail(LoginRequiredMixin, DetailView):
    model = Tipo
    template_name = "cadastros/detail/marca.html"

class CidadeDetail(LoginRequiredMixin, DetailView):
    model = Cidade
    template_name = "cadastros/detail/marca.html"

class UfDetail(LoginRequiredMixin, DetailView):
    model = Uf
    template_name = "cadastros/detail/marca.html"

class CachacaDetail(LoginRequiredMixin, DetailView):
    model = Cachaca
    template_name = "cadastros/detail/marca.html"