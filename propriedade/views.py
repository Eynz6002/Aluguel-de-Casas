from django.shortcuts import render, redirect
from django.http import request
from django.contrib import auth
from propriedade.models import Propriedade
from django.http import HttpResponse

# Create your views here.
def cadastrar_propriedade(request):
    proprietario = auth.get_user(request)

    if proprietario.tipo == 'P':
        if request.method == 'POST':
            titulo = request.POST.get('nome')
            descricao = request.POST.get('descricao')
            preco = request.POST.get('preco')
            foto = request.FILES.get('foto')
            endereco = request.POST.get('endereco')

            if not titulo or not descricao or not preco or not endereco:
                return redirect('/proprietario/cadastrar/?status=1')
            
            nova_propriedade = Propriedade(
                titulo=titulo,
                descricao=descricao,
                preco=preco,
                foto=foto,
                endereco=endereco,
                proprietario=proprietario
            )
            nova_propriedade.save()
            return redirect('/proprietario/cadastrar/?status=0')
        else:
            status = request.GET.get('status')
            return render(request, 'telas/casas.html', {'status': status})
    else:
        return HttpResponse('Você não tem acesso à essa página.')