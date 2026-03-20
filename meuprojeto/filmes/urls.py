from django.urls import path
from . import views

urlpatterns = [
    path("alugar/<str:titulo>/", views.alugarFilmeFormView, name="alugar_filme"),
    path("buscar/", views.buscarFilmesFormView, name="buscar_filmes"),
    path("meus-alugueis/", views.listarAlugueisView, name="meus_alugueis"),
    path("cancelar-aluguel/<int:aluguel_id>/", views.cancelarAluguelView, name="cancelar_aluguel"),
    path("cadastro-endereco/", views.cadastroEnderecoFormView, name="cadastro_endereco"),
]