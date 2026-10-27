from django import forms
from .models import banco_de_dados
from .models import Reserva
from django.utils import timezone

class banco_de_dadosForm(forms.ModelForm):
    class Meta:
        model = banco_de_dados
        fields = ['imagem', 'usuario', 'promocao', 'produto', 'categoria', 'gerenciamento', 'reserva']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva

        fields = [
            'nome_reserva',
            'telefone',
            'email',
            'data_reserva',
            'horario',
            'qtnde_pessoas',
            'observacao'
        ]

        widgets = {
            'data_reserva': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'horario': forms.TimeInput(
                attrs={'type': 'time'}
            ),
            'observacao': forms.Textarea(
                attrs={'rows': 3}
            )
        }

    def clean_data_reserva(self):
        data = self.cleaned_data.get('data_reserva')

        if data and data < timezone.localdate():
            raise forms.ValidationError(
                "Não é possível reservar uma data que já passou."
            )
    def clean_qtnde_pessoas(self):
        quantidade = self.cleaned_data.get('qtnde_pessoas')

        if quantidade is not None and quantidade < 1:
            raise forms.ValidationError(
                "A reserva deve ter pelo menos uma pessoa."
            )

        return quantidade
