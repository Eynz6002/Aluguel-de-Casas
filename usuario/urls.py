from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.login, name='logar'),
    path("cadastro/", views.cadastrar, name='cadastrar'),
]