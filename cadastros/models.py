from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Aqui será criado os models (classes) com seus atributos
class Tipo(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"
    
class Uf(models.Model):
    nome = models.CharField(max_length=2, verbose_name="UF")
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"
        
class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Cidade")
    uf = models.ForeignKey(Uf, on_delete=models.PROTECT, help_text="Selecione o estado da cidade de origem")

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.uf}"
    
class Cachaca(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, help_text="Selecione o tipo da bebida")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    ano = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)], verbose_name="Ano de Fabricação")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, help_text="Selecione a cidade de origem")
    teor = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name="Teor Alcoólico")
    observacoes = models.CharField(max_length=255, verbose_name="Observações")

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nome: {self.nome} | Marca: {self.marca} | Ano de Fabricação: {self.ano}"