from django.db import models
from django.conf import settings

class banco_de_dados(models.Model):
    imagem = models.CharField('imagem', max_length=100)
    usuario = models.CharField('usuario', max_length=100)
    promocao = models.CharField('promocao', max_length=100)
    produto = models.CharField('produto', max_length=100)
    categoria = models.CharField('categoria', max_length=100)
    gerenciamento = models.CharField('gerenciamento', max_length=100)
    reserva = models.CharField('reserva', max_length=100)


class Categoria(models.Model):
    nome_categoria = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.nome_categoria



class Produto(models.Model):
    descricao = models.CharField(max_length=200)

    detalhes = models.TextField(
        blank=True
    )

    valor_produto = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    preco_sob_consulta = models.BooleanField(
        default=False
    )

    disponivel = models.BooleanField(
        default=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos'
    )

    def __str__(self):
        return self.descricao



class Imagem(models.Model):
    descricao_imagem = models.CharField(max_length=200)

    arquivo = models.ImageField(
        upload_to='imagens/',
        blank=True,
        null=True
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='imagens',
        null=True,
        blank=True  
    )

    def __str__(self):
        return self.descricao_imagem


class Promocao(models.Model):
    descricao = models.TextField()

    imagem_promocao = models.ImageField(
        upload_to='promocoes/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.descricao[:50]


class Reserva(models.Model):
    nome_reserva = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    data_reserva = models.DateField()
    horario = models.TimeField()

    qtnde_pessoas = models.PositiveIntegerField()

    observacao = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('confirmada', 'Confirmada'),
            ('rejeitada', 'Rejeitada'),
            ('cancelada', 'Cancelada')
        ],
        default='pendente'
    )

    def __str__(self):
        return self.nome_reserva


class Gerenciamento(models.Model):
    TIPOS_ACAO = [
        ('adicionar', 'Adicionar usuário'),
        ('remover', 'Remover usuário'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='gerenciamentos'
    )

    acao = models.CharField(
        max_length=20,
        choices=TIPOS_ACAO
    )

    data_acao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.get_acao_display()} - {self.data_acao}"


# Create your models here.
