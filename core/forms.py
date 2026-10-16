from django import forms
from .models import banco_de_dados 

class banco_de_dadosForm(forms.ModelForm):
    class Meta:
        model = banco_de_dados
        fields = ['imagem', 'usuario', 'promocao', 'produto', 'categoria', 'gerenciamento', 'reserva']