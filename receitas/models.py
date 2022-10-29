from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class receita(models.Model):
    nome_receita = models.CharField(max_length=50)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimetno = models.TextField(max_length=40)
    categoria = models.CharField(max_length=40)
    data = models.DateTimeField(default=datetime.now, blank=True)
