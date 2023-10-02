from rest_framework.serializers import ModelSerializer
from ourfood.models import Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email']