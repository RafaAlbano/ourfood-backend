from django.db import models

class Sobremesas(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)