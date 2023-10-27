from rest_framework.serializers import ModelSerializer, CharField

from ourfood.models import Pedido


class PedidoSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)

    class Meta:
        model = Pedido
        fields = "__all__"
