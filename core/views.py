from django.shortcuts import render, redirect
from .models import banco_de_dados
from .forms import banco_de_dadosForm

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