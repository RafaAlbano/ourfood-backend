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
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens")
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=4, decimal_places=2)

    # def __str__(self):
    #     return f"ItemPedido {self.id} - Produto: {self.produto.nome}, Pedido: {self.pedido.id}, Quantidade: {self.quantidade}, Preço: {self.preco}"


