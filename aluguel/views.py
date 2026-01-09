from django.shortcuts import render, redirect
from propriedade.models import Propriedade
from usuario.models import Usuario
from django.http import Http404, HttpResponse
from django.contrib import auth

# Create your views here.
def alugar_casa(request):
    cliente = auth.get_user(request)
    if cliente.tipo == 'I':
        casas_alugáveis = Propriedade.objects.filter(
            disponivel=True
        )
        propriedades = {
            'propriedades': casas_alugáveis
        }
        return render(request, 'telas/clientes.html', propriedades)
    else:
        return HttpResponse('Você não tem acesso à essa página.')

def confirmar_aluguel(request, id):
    try:
        propriedade = Propriedade.objects.get(id=id)
    except Propriedade.DoesNotExist:
        raise Http404("Casa não encontrada")
    
    propriedade.disponivel = False
    propriedade.save()
    
    return redirect('/inquilino/alugar/')