from rest_framework.serializers import ModelSerializer
from ourfood.models import Pagamento

class PagamentoSerializer(ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['produto', 'valor']