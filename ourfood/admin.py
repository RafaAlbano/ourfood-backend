from django.contrib import admin

from .models import Categoria
from .models import Cliente
from .models import Pedido
from .models import Produto
from .models import ItemPedido
from .models import FomaDePagamento

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(ItemPedido)
admin.site.register(FomaDePagamento)