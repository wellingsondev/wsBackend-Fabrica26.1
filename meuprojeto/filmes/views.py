import requests  
from django.shortcuts import render 
from .models import Filme

def buscarFilmesFormView(request):

    nome = request.GET.get('nome')

    if not nome:
        return render(request, 'filmes/buscar.html', {"erro": "Por favor, informe o nome do filme."})
    
    try: 
        url = f'http://www.omdbapi.com/?t={nome}&apikey=9b1c8e5c'
        response = requests.get(url)
        response.raise_for_status()

        dados = response.json() 

    except Exception:

        return  render(request, 'filmes/buscar.html', {"erro": "Ocorreu um erro ao buscar o filme. Tente novamente mais tarde."})
    
    if dados.get('Response') == 'False':
        return render(request, 'filmes/buscar.html', {"erro": "Filme    não encontrado."})
    
        
    filme, created = Filme.objects.get_or_create(
        titulo=dados.get('Title'),
        defaults={
            'diretor': dados.get('Director'),
            'ano_lancamento': dados.get('Year'),
            'genero': dados.get('Genre'),
            'Ratings': float(dados.get('imdbRating', 0)),
            'Poster': dados.get('Poster')
        }
    )

    return render(request, 'filmes/filme.html', {'filme': filme})



# Create your views here.
