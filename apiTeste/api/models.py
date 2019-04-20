from django.db import models

# Create your models here.


UNIDADES_CHOICES = (
    ("UN", "Unidades"),
    ("KG", "Quilogramas"),
    ("M", "Metros" ),
    ("SC", "Sacos"),
    ("L", "Litros"),
    ("ML", "Mililitros"),
    ("M2", "Metros quadrados"),
    ("CM", "Centímetros")
)


class Produto(models.Model):
    descricao = models.TextField(null=False)
    nome_reduzido = models.CharField(max_length=24, null=False)
    unidade = models.CharField(choices=UNIDADES_CHOICES, max_length=3, null=False)
    fornecedor = models.TextField(null=False)
    fabricante = models.TextField(null=False)
    ean = models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.descricao
