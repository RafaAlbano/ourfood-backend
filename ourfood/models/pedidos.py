from django.db import models
from ourfood.models.clientes import Cliente  

class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=225)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - {self.cliente.nome} - {self.status} - {self.data_hora}"