from django.db import models

class banco_de_dados(models.Model):
    imagem = models.CharField('imagem', max_length=100)
    usuario = models.CharField('usuario', max_length=100)
    promocao = models.CharField('promocao', max_length=100)
    produto = models.CharField('produto', max_length=100)
    categoria = models.CharField('categoria', max_length=100)
    gerenciamento = models.CharField('gerenciamento', max_length=100)
    reserva = models.CharField('reserva', max_length=100)
    

# Create your models here.
