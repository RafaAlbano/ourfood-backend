from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from ourfood.models import Bebidas
from ourfood.serializers import BebidasSerializer

class BebidasViewSet(ModelViewSet):
    queryset = Bebidas.objects.all()
    serializer_class = BebidasSerializer