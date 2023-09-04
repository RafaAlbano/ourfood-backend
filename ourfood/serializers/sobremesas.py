from rest_framework.serializers import ModelSerializer

from ourfood.models import Sobremesas

class SobremesasSerializer(ModelSerializer):
    class Meta:
        model = Sobremesas
        fields = "__all__"