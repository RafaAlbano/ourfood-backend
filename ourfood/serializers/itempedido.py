from rest_framework.serializers import ModelSerializer
from ourfood.models import ItemPedido

class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'pedido', 'quantidade', 'preco']
    

