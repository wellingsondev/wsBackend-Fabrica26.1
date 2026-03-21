from django.shortcuts import render, redirect
from .models import Favorito
import requests

def index(request):

    response = requests.get("https://hp-api.onrender.com/api/characters")
    personagens = response.json()
    return render(request, 'meuapp/index.html', {'personagens': personagens[:24]})


def adicionar_favorito(request):
    if request.method == "POST":
        
        Favorito.objects.create(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
            house=request.POST.get('house'),
            actor=request.POST.get('actor')
        )
    return redirect('listar_favoritos')

def listar_favoritos(request):
    favoritos = Favorito.objects.all().order_by('-date_added')
    return render(request, 'meuapp/favoritos.html', {'favoritos': favoritos})

def remover_favorito(request, fav_id):
    favorito = Favorito.objects.get(id=fav_id)
    favorito.delete()
    return redirect('listar_favoritos')

def detalhe_bruxo(request, bruxo_id):

    import random
    res_char = requests.get(f"https://hp-api.onrender.com/api/character/{bruxo_id}")
    p = res_char.json()[0]
    res_spells = requests.get("https://hp-api.onrender.com/api/spells")
    spells_data = res_spells.json()
    
    feitico = random.choice(spells_data) if spells_data else {"name": "Expecto Patronum", "description": "Cria uma barreira de energia contra dementadores."}

    return render(request, 'meuapp/detalhe.html', {
        'p': p, 
        'feitico': feitico
    })