from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar_propriedade, name='cadastrar-propriedade'),
    path("tela-proprietario/", views.tela_proprietario, name='tela-do-proprietario'),
    path("propriedades/", views.listar_casas_proprietario, name='listar-propriedades'),
    path("desalugar/<int:id>", views.desalugar, name='desalugar')
]