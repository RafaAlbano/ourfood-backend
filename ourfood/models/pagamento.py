from django.db import models
from ourfood.models import Pedido

class Pagamento(models.Model):
    produto = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.valor}"