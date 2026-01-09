from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'telas/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            usuario = Usuario.objects.get(username=email)
            if check_password(senha, usuario.password):
                
                auth.login(request, usuario)
                if usuario.tipo == 'I':
                    return redirect('/inquilino/alugar')
                elif usuario.tipo == 'P':
                    return redirect('/proprietario/cadastrar')
            else:
                return redirect('/auth/login/?status=2')
                
        except Usuario.DoesNotExist:
            return redirect('/auth/login/?status=1')

def cadastrar(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'telas/cadastro.html', {'status': status})
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        tipo = request.POST.get('tipo')

        if not email or not senha or not tipo:
            return redirect('/auth/cadastro/?status=5')
        
        if Usuario.objects.filter(email=email).exists():
            return redirect('/auth/cadastro/?status=4')
        
        if len(senha) < 8:
            return redirect('/auth/cadastro/?status=1')
        elif len(senha) > 16:
            return redirect('/auth/cadastro/?status=2')
        elif senha != confirmar_senha:
            return redirect('/auth/cadastro/?status=3')

        try:
            novo_usuario = Usuario(
                email=email,
                username=email,
                password=make_password(senha),
                tipo=tipo
            )
            novo_usuario.save()
            return redirect('/auth/cadastro/?status=0')
        except Exception:
            return redirect('/auth/cadastro/?status=6')