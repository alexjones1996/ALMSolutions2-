from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Entrada


def financeiro(request):
    #Retorna do BD as 10 ultimas entradas financeiras
    ultimas_entradas_financeiras = Entrada.objects.order_by('-data_entrada')[:10]
    resposta_de_valores_bd = { 'ultimas_entradas_financeiras': ultimas_entradas_financeiras,}
    
    return render(request, 'financeiro/financeiro.html', resposta_de_valores_bd)


    #template = loader.get_template('financeiro/financeiro.html')
    #resposta_http = ', '.join([str(q.valor_entrada) for q in ultimas_entradas_financeiras])
    #return HttpResponse(template.render(resposta_valores_bd, request))

def entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk=entrada_id)
    return render(request, 'financeiro/financeiro.html', {'entrada' : entrada})
