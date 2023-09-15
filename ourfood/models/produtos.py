from django.db import models

from uploader.models import Image
from ourfood.models import Categoria


class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produtos"
    )

    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.titulo} ({self.categoria}) ({self.quantidade}) ({self.preco})"
