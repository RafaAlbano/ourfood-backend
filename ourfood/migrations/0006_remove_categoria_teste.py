# Generated by Django 4.2.5 on 2023-09-13 17:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ourfood", "0005_categoria_teste"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categoria",
            name="teste",
        ),
    ]
