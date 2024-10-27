from django.db import models

class User(models.Model):
    nomeUser = models.CharField(max_length=100)
    senhaUser = models.CharField(max_length=20)

class Citacao(models.Model):
    conteudo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
