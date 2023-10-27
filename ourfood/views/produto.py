from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from ourfood.models import Produto
from ourfood.serializers import ProdutoDetailSerializer, ProdutoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria__descricao"]


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProdutoDetailSerializer
        return ProdutoSerializer