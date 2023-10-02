from rest_framework import serializers
from ourfood.models import ItemPedido

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'pedido', 'quantidade']
    
# serializer = ItemPedidoSerializer(data=dados_do_pedido)
