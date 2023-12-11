from rest_framework.serializers import ModelSerializer, CharField
from ourfood.models import Pedido, ItemPedido, Produto

class ProdutoItemSerializer(ModelSerializer):
   imagem = CharField(source='capa.url')
   class Meta:
      model = Produto
      fields = ['id', 'nome', 'preco', 'imagem']

class ItemPedidoSerializer(ModelSerializer):
    produto = ProdutoItemSerializer()
    class Meta:
        # total = SerializerMethodField()
        model = ItemPedido
        fields = ["produto", "quantidade"]
        # fields="__all__"
        depth = 2

        def get_total(self, instance):
          return instance.quantidade * instance.pedido.preco