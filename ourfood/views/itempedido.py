from rest_framework.viewsets import ModelViewSet
from ourfood.models import ItemPedido
from ourfood.serializers import ItemPedidoSerializer

class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    
