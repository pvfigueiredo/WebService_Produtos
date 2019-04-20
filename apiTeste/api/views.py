from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .models import *
from .pagination import *



class ProdutoList(APIView):
    def get(self, request):
        try:
            lista_produtos = Produto.objects.all()
            paginator = PaginacaoProduto()
            result_page = paginator.paginate_queryset(lista_produtos, request)
            serializer = SerializerProduto(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor!!!"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SerializerProduto(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor!!!"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProdutoModifica(APIView):
    def get(self, request, pk):
        try:
            if pk == 0:
                return JsonResponse({"mensagem": "O ID deve ser maior que 0."}, status=status.HTTP_400_BAD_REQUEST)
            produto = Produto.objects.get(pk=pk)
            serializers = SerializerProduto(produto)
            return Response(serializers.data)
        except Produto.DoesNotExist:
            return JsonResponse({"mensagem": "Produto inexistente!"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return  JsonResponse({"mensagem": "Ocorreu um erro no servidor!!!"},
                                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, pk):
        try:
            if pk == 0:
                return JsonResponse({"mensagem": "O ID deve ser maior que 0."}, status=status.HTTP_400_BAD_REQUEST)
            produto = Produto.objects.get(pk=pk)
            serializers = SerializerProduto(produto, request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Produto.DoesNotExist:
            return JsonResponse({"mensagem": "Produto inexistente."}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Erro no servidor!!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == 0:
                return JsonResponse({"mensagem": "O ID deve ser maior que 0."}, status=status.HTTP_400_BAD_REQUEST)
            produto = Produto.objects.get(pk=pk)
            produto.delete()
            return JsonResponse({"mensagem": "Produto apagado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Produto.DoesNotExist:
            return JsonResponse({"mensagem": "Produto inexistente."}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Erro no servidor!!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
