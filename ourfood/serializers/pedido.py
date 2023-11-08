from rest_framework.serializers import ModelSerializer, CharField
from ourfood.models import Pedido, ItemPedido 
from ourfood.serializers import ItemPedidoSerializer
from rest_framework import serializers

class PedidoSerializer(ModelSerializer):
    itens = ItemPedidoSerializer(many=True)
    status = CharField(source="get_status_display")
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
    # itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ("usuario", "status", "total")

    def create(self, validated_data):
        itens= validated_data.pop("itens")
        pedido = Pedido.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["livro"].preco # Coloca o preço do livro no item de compra
            ItemPedido.objects.create(pedido=pedido, **item)
        pedido.save()
        return pedido
    
    def validate(self, data):
        if data["quantidade"] > data["livro"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "Quantidade solicitada não disponível em estoque."}
            )
        return data