from django.shortcuts import render
from django.http import HttpResponse

def HelloWorld(request):
    return(HttpResponse('<h1>Hello World<h1/>'))

def index(request):
    return render(request, 'index.html')

def base(request):
    lista = [1, 2, 3, 4, 5]
    mensagem_inicial = "comecando o loop"
    mensagem_final = "terminando o loop"
    return render(request, 'base.html', {'lista': lista, "mensagem_inicial": mensagem_inicial, "mensagem_final": mensagem_final})