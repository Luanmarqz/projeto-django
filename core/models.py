
from django.db import models

# Create your models here.
class Ocorrencia(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em Andamento'),
        ('resolvida', 'Resolvida'),
    ]
    
    descricao = models.CharField(max_length=200)
    local = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.descricao
    