from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ourfood.models import Pedido, ItemPedido

class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        # total = SerializerMethodField()
        model = ItemPedido
        fields = ["pedido", "quantidade"]
        # fields="__all__"
        depth = 2

        def get_total(self, instance):
          return instance.quantidade * instance.pedido.preco