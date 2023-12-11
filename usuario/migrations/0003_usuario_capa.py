# Generated by Django 4.2.7 on 2023-12-10 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("usuario", "0002_alter_usuario_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="capa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]