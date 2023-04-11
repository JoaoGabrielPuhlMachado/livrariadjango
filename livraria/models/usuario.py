from django.db import models
from django.contrib.auth.models import AbstractUser
from uploader.models import Image

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )