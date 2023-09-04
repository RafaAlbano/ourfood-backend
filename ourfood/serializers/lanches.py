from rest_framework.serializers import ModelSerializer

from ourfood.models import Lanches

class LanchesSerializer(ModelSerializer):
    class Meta:
        model = Lanches
        fields = "__all__"