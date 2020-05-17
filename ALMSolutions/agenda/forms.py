from django import forms
from .models import Evento

class FormularioEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'tipo', 'descricao_evento', 'valor_evento', 'data_evento']