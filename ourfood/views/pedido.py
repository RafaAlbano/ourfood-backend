from rest_framework.viewsets import ModelViewSet

from ourfood.models import Pedido
from ourfood.serializers import PedidoSerializer, CriarEditarPedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()     

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'put':
            return CriarEditarPedidoSerializer
        return PedidoSerializer
    
    def get_queryset(self):
        usuario = self.request.user
        if usuario.id is None:
            return Pedido.objects.all()
        if usuario.is_superuser:
            return Pedido.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Pedido.objects.all()
        return Pedido.objects.filter(usuario=usuario)