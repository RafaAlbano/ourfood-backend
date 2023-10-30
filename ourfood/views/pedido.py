from rest_framework.viewsets import ModelViewSet

from ourfood.models import Pedido
from ourfood.serializers import PedidoSerializer
from ourfood.serializers import  CriarEditarPedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarPedidoSerializer
        return PedidoSerializer