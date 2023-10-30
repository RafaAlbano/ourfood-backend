from django.db import models
from usuario.models import Usuario
from ourfood.models import Produto

class Pedido(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = (1,"Carrinho",)
        REALIZADO = (2,"Realizado",)
        PAGO = (3,"Pago",)
        ENTREGUE = (4,"Entregue",)

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)   

    @property
    def total(self):
        # total = 0
        # for item in self.itens.all():
        # total += item.livro.preco * item.quantidade
        # return total
        return sum(item.pedido.preco * item.quantidade for item in self.itens.all())
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens")
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=4, decimal_places=2)

