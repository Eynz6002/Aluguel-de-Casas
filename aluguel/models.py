from django.db import models
from propriedade.models import Propriedade, Usuario

# Create your models here.
class Aluguel(models.Model):
    inquilino = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    dias_alugados = models.DateField()
    total_pago = models.IntegerField()
    encerrado = models.BooleanField()