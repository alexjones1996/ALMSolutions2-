from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'financeiro/index.html')
    #return HttpResponse("Bem vindo ao sistema ALMSolutions")