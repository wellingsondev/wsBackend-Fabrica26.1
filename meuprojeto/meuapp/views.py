from django.shortcuts import render, redirect
from .models import Favorito
import requests
from django.contrib import messages



def index(request):
    casa_selecionada = request.GET.get('casa', '') # Pega a casa escolhida
    
    response = requests.get("https://hp-api.onrender.com/api/characters")
    personagens = response.json() if response.status_code == 200 else []

    # Se uma casa foi escolhida, filtramos a lista antes de enviar para o HTML
    if casa_selecionada:
        personagens = [p for p in personagens if p['house'] == casa_selecionada]

    return render(request, 'meuapp/index.html', {
        'personagens': personagens[:24],
        'casa_selecionada': casa_selecionada
    })

def adicionar_favorito(request):
    if request.method == "POST":
        nome = request.POST.get('name')
        image = request.POST.get('image')
        casa = request.POST.get('house')
        ator = request.POST.get('actor')
        ja_existe = Favorito.objects.filter(nome=request.POST.get('name')).exists()

        if not ja_existe and nome and image:
            Favorito.objects.create(
                nome =request.POST.get('name'),
                image=request.POST.get('image'),
                casa =request.POST.get('house'),
                ator=request.POST.get('actor')
            )
            messages.success(request, f"{nome} adicionado aos favoritos!")
        else:

            messages.warning(request, f"{nome} já está nos favoritos ")  
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