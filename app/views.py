from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def puberdade(request):
    return render(request, 'puberdade.html')

def topicos(request):
    return render(request, 'topicos.html')

def imagens(request):
    return render(request, 'imagens.html')
