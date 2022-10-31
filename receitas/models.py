from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=50)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimetno = models.TextField(max_length=40)
    categoria = models.CharField(max_length=40)
    data = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)