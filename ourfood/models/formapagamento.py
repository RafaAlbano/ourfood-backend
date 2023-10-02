from django.db import models
from ourfood.models import Pagamento

class FomaDePagamento(models.Model):
    produto = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao