
from django.urls import path
from .views import *



urlpatterns = [
    path('produtos', ProdutoList.as_view()),
    path('produtos/<int:pk>', ProdutoModifica.as_view()),
]