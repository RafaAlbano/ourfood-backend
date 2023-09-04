from rest_framework.serializers import ModelSerializer

from ourfood.models import Bebidas

class BebidasSerializer(ModelSerializer):
    class Meta:
        model = Bebidas
        fields = "__all__"