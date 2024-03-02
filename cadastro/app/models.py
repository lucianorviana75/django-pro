from django.db import models

# Create your models here.


class Carro(models.Model):
    carro = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    ano = models.IntegerField()
    
    def __str__(self) -> str:
        return self.carro
        