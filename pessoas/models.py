from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)