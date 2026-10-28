from django.shortcuts import render, redirect
from .models import banco_de_dados, Produto, Categoria
from .forms import banco_de_dadosForm, ReservaForm
from django.db.models import Prefetch

def listar_tabelas(request):
    bdd = banco_de_dados.objects.all()
    contexto = {
        'todos_bdd': bdd
    }
    return render(request, 'banco_de_dados.html', contexto)

def cadastrar_bdd(request):
    form = banco_de_dadosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_tabelas')
        
    contexto = {
        'form_bdd': form
    }
    return render(request, 'bdd_cadastrar.html', contexto)

def pagina_inicial(request):
    return render(request, 'index.html')

def pagina_contatos(request):
    return render (request, 'cont.html')


def cardapio(request):
    produtos = Produto.objects.select_related('categoria').all()

    contexto = {
        'produtos': produtos
    }

    return render(request, 'cardapio.html', contexto)

def pagina_localizacao(request):
    return render (request, 'loc.html')

def pagina_funcionario(request):
    if request.method == 'POST':
        return redirect('inicio_funcionario')

    return render(request, 'funcionario.html')


def cardapio_teste(request):
    categorias = Categoria.objects.filter(
        produtos__disponivel=True
    ).distinct().prefetch_related(
        Prefetch(
            'produtos',
            queryset=Produto.objects.filter(disponivel=True)
        )
    )

    return render(request, 'cardapio_teste.html', {
        'categorias': categorias
    })

def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reserva_sucesso')
    else:
        form = ReservaForm()

    return render(request, 'reserva.html', {
        'form': form
    })


def reserva_sucesso(request):
    return render(request, 'reserva_sucesso.html')

def promocoes(request):
    return render(request, 'promocoes.html')

def inicio_funcionario(request):
    return render(request, 'inicio_funcionario.html')
