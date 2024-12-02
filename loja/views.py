from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto

def home(request):
    return render(request, 'loja/home.html')

def cadastro(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem')  # Ajuste na URL nomeada correta
    else:
        form = ProdutoForm()

    return render(request, 'loja/cadastro.html', {'form': form})

def listagem(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/listagem.html', {'produtos': produtos})

def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('listagem')
