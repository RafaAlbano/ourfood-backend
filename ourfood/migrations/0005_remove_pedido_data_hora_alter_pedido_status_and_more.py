# Generated by Django 4.2.6 on 2023-10-25 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ourfood", "0004_remove_itempedido_pedido_alter_itempedido_produto_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedido",
            name="data_hora",
        ),
        migrations.AlterField(
            model_name="pedido",
            name="status",
            field=models.IntegerField(
                choices=[
                    (1, "Carrinho"),
                    (2, "Realizado"),
                    (3, "Pago"),
                    (4, "Entregue"),
                ],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="compras",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
