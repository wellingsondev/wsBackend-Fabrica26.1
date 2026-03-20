from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=50)
    Ratings = models.FloatField()
    Poster = models.URLField()

    def __str__(self):
        return f"{self.titulo} - {self.genero}"
    
class Aluguel(models.Model):

    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_aluguel = models.DateField(default=timezone.now)
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f"{self.usuario.username} alugou {self.filme.titulo}"

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10) 
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    