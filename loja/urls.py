from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listagem/', views.listagem, name='listagem'),
    path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
]
