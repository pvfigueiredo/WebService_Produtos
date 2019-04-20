from rest_framework import serializers
from .models import *


class SerializerProduto(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "descricao", "nome_reduzido", "unidade", "fornecedor", "fabricante", "ean"]
