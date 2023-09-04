from rest_framework.viewsets import ModelViewSet

from ourfood.models import Produto
from ourfood.serializers import ProdutoDetailSerializer, ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProdutoDetailSerializer
        return ProdutoSerializer