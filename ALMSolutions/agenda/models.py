from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)
    descricao_evento = models.CharField(max_length= 1000)
    valor_evento = models.DecimalField (max_digits=10, decimal_places=2)
    data_evento = models.DateTimeField ('Data do evento')

