from rest_framework.viewsets import ModelViewSet

from ourfood.models import Pedido
from ourfood.serializers import PedidoSerializer
from ourfood.serializers import  CriarEditarPedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Pedido.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Pedido.objects.all()
        return Pedido.objects.filter(usuario=usuario)