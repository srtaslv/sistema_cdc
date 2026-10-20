
from django.contrib import admin
from .models import (
    Categoria,
    Produto,
    Imagem,
    Promocao,
    Reserva,
    Gerenciamento
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    search_fields = ('nome_categoria',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'descricao',
        'valor_produto',
        'categoria'
    )
    list_filter = ('categoria',)
    search_fields = ('descricao',)


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao_imagem')
    search_fields = ('descricao_imagem',)


@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_reserva',
        'data_reserva',
        'horario',
        'qtnde_pessoas',
        'status'
    )
    list_filter = ('status', 'data_reserva')
    search_fields = ('nome_reserva', 'telefone')

@admin.register(Gerenciamento)
class GerenciamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'acao',
        'data_acao'
    )

    list_filter = ('acao', 'data_acao')
    readonly_fields = ('data_acao',)

