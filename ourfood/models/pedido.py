from django.db import models
from usuario.models import Usuario

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.CharField(max_length=225)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - {self.usuario.first_name} - {self.status} - {self.data_hora}"