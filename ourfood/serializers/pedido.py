from rest_framework.serializers import ModelSerializer, CharField
from ourfood.models import Pedido

class PedidoSerializer(ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)
    # status = CharField(source="get_status_display", read_only=True)
    usuario = CharField(source="usuario.email", read_only=True)

    class Meta:
        model = Pedido
        fields = "__all__"
