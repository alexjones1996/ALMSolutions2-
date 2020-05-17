from django.shortcuts import render, redirect
from .forms import FormularioEvento
from .models import Evento


def consulta_evento(request):
    agenda_eventos = Evento.objects.all()
    return render(request, 'agenda/agenda.html', {'agenda_eventos' : agenda_eventos})


def criar_evento(request):
    form = FormularioEvento(request.POST or None)

    #Valida se o formulario está em branco
    if form.is_valid():
        form.save()
        return redirect ('/agenda' )
    return render(request, 'agenda/formulario-evento.html', {'form':form})