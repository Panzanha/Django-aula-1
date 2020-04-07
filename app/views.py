from django.shortcuts import render
from django.http import HttpResponse
from .models import Bixo

def HelloWorld(request):
    return(HttpResponse('<h1>Hello World<h1/>'))

def index(request):
    return render(request, 'index.html')

def base(request):
    lista = [1, 2, 3, 4, 5]
    mensagem_inicial = "comecando o loop"
    mensagem_final = "terminando o loop"
    return render(request, 'base.html', {'lista': lista, "mensagem_inicial": mensagem_inicial, "mensagem_final": mensagem_final})

def bixos(request):
    bixos = Bixo.objects.all()
    mensagem = "Xupa bixaral"
    return render(request, 'bixos.html', {'bixos': bixos, "mensagem": mensagem})