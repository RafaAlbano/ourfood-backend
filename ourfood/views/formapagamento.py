from rest_framework.viewsets import ModelViewSet

from ourfood.models import FomaDePagamento
from ourfood.serializers import FormaDePagamentoSerializer


class FormaDePagamentoViewSet(ModelViewSet):
    queryset = FomaDePagamento.objects.all()
    serializer_class = FormaDePagamentoSerializer