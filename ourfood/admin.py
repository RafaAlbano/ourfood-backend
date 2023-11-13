from django.contrib import admin

from .models import Categoria
from .models import Pedido
from .models import Produto
from .models import ItemPedido

admin.site.register(Categoria)
admin.site.register(Produto)
# admin.site.register(ItemPedido)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido

@admin.register(Pedido)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]