import requests  
from django.shortcuts import get_object_or_404, redirect, render 
from .models import Aluguel, Filme, Perfil
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

@login_required
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

def alugarFilmeFormView(request, titulo):

    filme = get_object_or_404(Filme, titulo__iexact = titulo)

    data_devolucao = timezone.now() + timedelta(days=3)

    Aluguel.objects.create(

        usuario = request.user,  
        filme = filme,
        data_devolucao=data_devolucao

    )

    return redirect("meus_alugueis")

@login_required
def listarAlugueisView(request):

    alugueis = Aluguel.objects.filter(usuario=request.user)

    return render(request, 'filmes/listar_alugueis.html', {'alugueis': alugueis})


def cancelarAluguelView(request, aluguel_id):

    aluguel = get_object_or_404(Aluguel, id=aluguel_id, usuario=request.user)

    aluguel.delete()

    return redirect("meus_alugueis")

def cadastroEnderecoFormView(request):  
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Perfil.objects.create(
                usuario = user,
                rua = request.POST.get('rua'),
                cidade = request.POST.get('cidade'),
                estado = request.POST.get('estado'),
                numero = request.POST.get('numero'),
                cep = request.POST.get('cep')
                
            )

            return redirect("meus_alugueis")

        return render(request, 'filmes/cadastro_endereco.html')
    
    else:
        form = UserCreationForm()
    
    return render(request, 'filmes/cadastro_endereco.html', {'form': form})


# Create your views here.
