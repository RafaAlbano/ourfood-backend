# Generated by Django 4.2.5 on 2023-09-06 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ourfood", "0003_categoria_delete_bebidas_delete_lanches_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=7, null=True
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="produtos",
                        to="ourfood.categoria",
                    ),
                ),
            ],
        ),
    ]
