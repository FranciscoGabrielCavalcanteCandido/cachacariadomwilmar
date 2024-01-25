from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/modelo.html"

class SobreView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/sobre.html"