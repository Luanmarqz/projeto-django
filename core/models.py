
from django.db import models

# Create your models here.
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=200)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    