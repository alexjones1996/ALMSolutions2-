from django.db import models

class Entrada(models.Model):
    valor_evento = models.DecimalField(decimal_places=2)
    data_evento = models.DateTimeField('Data do vento')

class Saida(models.Model):
    pagamento_parceiro = models.DecimalField(decimal_places=2)
    data_pagamento = models.DateTimeField('Data do pagamento')