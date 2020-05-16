from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Entrada, Saida


def financeiro(request):
    #Retorna do BD as 10 ultimas entradas financeiras
    ultimas_entradas_financeiras = Entrada.objects.order_by('-data_entrada')[:10]
    resposta_entrada_do_bd = { 'ultimas_entradas_financeiras': ultimas_entradas_financeiras,}
    
    #listar todas entradas
    #ultimas_entradas_financeiras = Entrada.objects.all()


    #Retorna do BD as 20 ultimas entradas financeiras
    ultimas_saidas_financeiras = Saida.objects.order_by('-data_saida')[:10]
    resposta_saida_do_bd = { 'ultimas_saidas_financeiras' : ultimas_saidas_financeiras}
   
    resposta_bd ={ 'resposta_entrada_do_bd' : resposta_entrada_do_bd, 'resposta_saida_do_bd' : resposta_saida_do_bd }
    return render(request, 'financeiro/financeiro.html', resposta_bd)


def entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk=entrada_id)
    return render(request, 'financeiro/financeiro.html', {'entrada' : entrada})


def saida(request, saida_id):
    saida = get_object_or_404(Saida, pk=saida_id)
    return render(request, 'financeiro/financeiro.html', {'saida' : saida})
