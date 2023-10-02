from django.db import models
from ourfood.models import Produto
from ourfood.models import Pedido

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"ItemPedido {self.id} - Produto: {self.produto.nome}, Pedido: {self.pedido.id}, Quantidade: {self.quantidade}, Preço: {self.preco}"
