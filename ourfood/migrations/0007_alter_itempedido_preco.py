# Generated by Django 4.2.6 on 2023-10-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ourfood", "0006_itempedido_pedido"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itempedido",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
