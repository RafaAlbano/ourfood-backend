from django.contrib import admin

from .models import Lanches, Bebidas, Sobremesas

admin.site.register(Lanches)
admin.site.register(Bebidas)
admin.site.register(Sobremesas)