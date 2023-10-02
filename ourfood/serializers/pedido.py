from rest_framework.serializers import ModelSerializer
from ourfood.models import Pedido

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'status', 'data_hora']
