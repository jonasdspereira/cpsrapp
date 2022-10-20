from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
