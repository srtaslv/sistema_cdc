"""
URL configuration for bancodedados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_tabelas, cadastrar_bdd, pagina_inicial, pagina_contatos, cardapio, pagina_localizacao, pagina_funcionario, cardapio_teste, cadastrar_reserva, reserva_sucesso, promocoes, inicio_funcionario

urlpatterns = [ 
    path('reservas/', cadastrar_reserva, name='cadastrar_reserva'),
    path('reserva-sucesso/', reserva_sucesso, name='reserva_sucesso'),
    path('cardapio-teste/', cardapio_teste, name='cardapio_teste'),
    path('funcionario/', pagina_funcionario, name='pagina_funcionario'),
    path('contatos/', pagina_contatos, name='pagina_contatos'),
    path('', pagina_inicial, name='pagina_inicial'),   
    path('cardapio/', cardapio, name='cardapio'),
    path('banco_de_dados/', listar_tabelas, name='listar_tabelas'),
    path('cadastrar_bdd/', cadastrar_bdd, name='cadastrar_bdd'),
    path('localizacao/', pagina_localizacao, name='pagina_localizacao'),
    path('promocoes/', promocoes, name='promocoes'),
    path('pagina-func/', inicio_funcionario, name='inicio_funcionario'),

    path('admin/', admin.site.urls),
]
