from django.shortcuts import render
from django.http import HttpResponse

def financeiro(request):
    return HttpResponse("Controle Financeiro")