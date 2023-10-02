from django.contrib import admin

from .models import Categoria
from .models import Cliente
from .models import Pedido
from .models import Produto

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Produto)
