from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

def loginView(request):
    if request.method == 'GET':
        return render(request, 'loginCadastro/login.html')
    elif request.method == 'POST':

        nome = request.POST['nomeUser']
        senha = request.POST['senhaUser']       

        try:
            user = User.objects.get(nomeUser=nome)   
            if user.senhaUser == senha:
                user_id = user.id

                request.session['user'] = user.nomeUser
                request.session['user_id'] = user_id
                return redirect('mainPage')

            else:
                return HttpResponse("<h1>SENHA DE USUÁRIO ERRADA!</h1>")
        except User.DoesNotExist:
            return HttpResponse("<h1>Nome de usuário não existe!</h1>")
   

def cadastroView(request):
    if request.method == 'GET':
        return render(request, 'loginCadastro/cadastro.html')
    elif request.method == 'POST':

        usuario = User()
        usuario.nomeUser = request.POST['nomeUser']
        usuario.senhaUser = request.POST['senhaUser']

        nome = request.POST['nomeUser']

        try:
            user = User.objects.get(nomeUser=nome)
            return HttpResponse("Usuário já cadastrado!")
        except User.DoesNotExist:
            
            usuario.save()
            return redirect('loginPage')
