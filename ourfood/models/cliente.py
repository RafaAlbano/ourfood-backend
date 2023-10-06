from django.db import models
from uploader.models import Image
from django.contrib.auth.models import AbstractUser


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    