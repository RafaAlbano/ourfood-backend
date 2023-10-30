from rest_framework.serializers import ModelSerializer, CharField
from ourfood.models import Pedido, ItemPedido 
from ourfood.serializers import ItemPedidoSerializer

class PedidoSerializer(ModelSerializer):
    itens = ItemPedidoSerializer(many=True)
    status = CharField(source="get_status_display")
    usuario = CharField(source="usuario.email")

    class Meta:
        model = Pedido
        fields = ("id", "usuario", "status", "total", "itens")

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItemPedido.objects.create(pedido=instance, **item)
        instance.save()
        return instance
       
class CriarEditarPedidoSerializer(ModelSerializer):
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ("usuario", "itens")
    
    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        pedido.save()
        return pedido
    
class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ("pedido", "quantidade")