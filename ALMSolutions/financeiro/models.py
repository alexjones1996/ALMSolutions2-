import datetime
from django.db import models
from django.utils import timezone

class Entrada(models.Model):
    valor_entrada = models.DecimalField(max_digits = 10, decimal_places=2)
    data_entrada = models.DateTimeField('Data do Recebimento')
    
    def __str__(self):
        return str(self.valor_entrada)

    def ultimas_entradas(self):
        return self.data_entrada >= timezone.now() - datetime.timedelta(month=31)


class Saida(models.Model):
    valor_saida = models.DecimalField(max_digits = 10, decimal_places=2)
    data_saida = models.DateTimeField('Data do Pagamento')

    def __str__(self):
        return self.valor_saida
    
    def ultimas_saidas(self):
        return self.data_saida >= timezone.now() - datetime.timedelta(month=31)

    