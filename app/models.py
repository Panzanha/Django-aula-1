from django.db import models

class Bixo(models.Model):
    Nome = models.CharField(max_length=50)
    Nome_de_Bixo = models.CharField(max_length=30)
    Idade = models.IntegerField()
    Ape = models.IntegerField()

    def __str__(self):
        return self.Nome_de_Bixo