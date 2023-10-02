from rest_framework.serializers import ModelSerializer
from ourfood.models import FomaDePagamento

class FormaDePagamentoSerializer(ModelSerializer):
    class Meta:
        model = FomaDePagamento
        fields = "__all__"