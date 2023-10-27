from rest_framework.viewsets import ModelViewSet

from ourfood.models import Pedido
from ourfood.serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer