from rest_framework.viewsets import ModelViewSet

from ourfood.models import Categoria
from ourfood.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer