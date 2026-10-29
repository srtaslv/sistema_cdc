from django.shortcuts import render, redirect
from .models import banco_de_dados, Produto, Categoria, Reserva
from .forms import banco_de_dadosForm, ReservaForm
from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

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

def reserva_funcionario(request):
    reservas = Reserva.objects.all().order_by(
        'data_reserva', 'horario'
    )

    busca = request.GET.get('busca', '').strip()

    if busca:
        reservas = reservas.filter(
            Q(nome_reserva__icontains=busca) |
            Q(email__icontains=busca)
        )

    filtro = request.GET.get('status', 'todas')

    if filtro == 'pendentes':
        reservas = reservas.filter(status='pendente')
    elif filtro == 'aprovadas':
        reservas = reservas.filter(status='confirmada')
    elif filtro == 'rejeitadas':
        reservas = reservas.filter(status='rejeitada')
    elif filtro == 'canceladas':
        reservas = reservas.filter(status='cancelada')

    contagens = {
        'todas': Reserva.objects.count(),
        'pendentes': Reserva.objects.filter(status='pendente').count(),
        'aprovadas': Reserva.objects.filter(status='confirmada').count(),
        'rejeitadas': Reserva.objects.filter(status='rejeitada').count(),
        'canceladas': Reserva.objects.filter(status='cancelada').count(),
    }

    reserva_id = request.GET.get('reserva')
    reserva_selecionada = None

    if reserva_id:
        reserva_selecionada = get_object_or_404(
            Reserva, pk=reserva_id
        )

    contexto = {
        'reservas': reservas,
        'busca': busca,
        'filtro': filtro,
        'contagens': contagens,
        'reserva_selecionada': reserva_selecionada,
    }

    return render(
        request,
        'reserva_funcionario.html',
        contexto
    )


@require_POST
def acao_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    acao = request.POST.get('acao')

    if acao == 'aprovar':
        reserva.status = 'confirmada'

    elif acao == 'rejeitar':
        reserva.status = 'rejeitada'

    elif acao == 'cancelar':
        reserva.status = 'cancelada'

    else:
        return redirect('reserva_funcionario')

    reserva.save(update_fields=['status'])

    return redirect(
        f'/funcionario/reservas/?reserva={reserva.pk}'
    )
