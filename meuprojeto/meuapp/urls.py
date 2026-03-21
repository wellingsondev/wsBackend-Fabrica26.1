from django.urls import path
from .views import index, listar_favoritos, detalhe_bruxo, adicionar_favorito, remover_favorito



urlpatterns = [
    path('index/', index, name='index'),
    path('favoritos/', listar_favoritos, name='listar_favoritos'),
    path('favoritos/adicionar/', adicionar_favorito, name='adicionar_favorito'),
    path('favoritos/remover/<int:fav_id>/', remover_favorito, name='remover_favorito'),
    path('bruxo/<str:bruxo_id>/', detalhe_bruxo, name='detalhe_bruxo'),
    
]
