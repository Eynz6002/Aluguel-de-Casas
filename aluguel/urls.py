from django.urls import path
from . import views

urlpatterns = [
    path("alugar/", views.alugar_casa, name='alugar-propriedade'),
    path("confirmar/<int:id>", views.confirmar_aluguel, name='confirmar-aluguel'),
]