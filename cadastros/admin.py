from django.contrib import admin

from .models import Tipo, Cidade, Uf, Cachaca

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Cidade)
admin.site.register(Uf)
admin.site.register(Cachaca)