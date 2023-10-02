from rest_framework.viewsets import ModelViewSet
from ourfood.models import Pagamento
from ourfood.serializers import PagamentoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer   
