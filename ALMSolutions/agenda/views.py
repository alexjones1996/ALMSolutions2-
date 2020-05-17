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


def atualizar_evento(request, id):
    evento = Evento.objects.get(id = id)
    form = FormularioEvento(request.POST or None, instance=evento)
    #Valida se o formulario está em branco
    if form.is_valid():
        form.save()
        return redirect ('/agenda')
    return render(request, 'agenda/formulario-evento.html', {'form': form, 'evento': evento })


def apagar_evento(request, id):
    evento = Evento.objects.get(id = id)
    if request.method == 'POST':
        evento.delete()
        return redirect ('/agenda')
    return render(request, 'agenda/apagar_evento.html', { 'evento': evento })
