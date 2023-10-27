from rest_framework.serializers import ModelSerializer
from ourfood.models import Pedido, ItemPedido

class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = "__all__"