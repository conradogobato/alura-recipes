from django.shortcuts import render, get_object_or_404
from .models import receita

def index(req):
    receitas = receita.objects.all()
    dados = {
        'receitas' : receitas
    }
    return render(req, 'receitas/index.html', dados)

def Receita(req, receita_id):
    Receita = get_object_or_404(receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : Receita
    }

    return render(req, 'receitas/receita.html', receita_a_exibir)