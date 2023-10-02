from rest_framework import serializers
from ourfood.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'status', 'data_hora']
