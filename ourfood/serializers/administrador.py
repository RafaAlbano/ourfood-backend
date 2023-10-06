from rest_framework.serializers import ModelSerializer
from ourfood.models import Administrador

class AdministradorSerializer(ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['id', 'nome', 'email']