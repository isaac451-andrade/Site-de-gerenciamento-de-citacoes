from django.shortcuts import render, redirect
from loginCadastro.models import *
def mainPage(request):
    citacoes = Citacao.objects.filter(usuario=request.session.get('user_id'))
    print(len(citacoes))
    if request.method == 'POST':
        conteudo = request.POST['quote']
        autor = request.POST['campo-autor']

        citacao = Citacao(conteudo=conteudo, autor=autor, usuario=User.objects.get(nomeUser=request.session.get('user')))

        citacao.save()
        
        return redirect('mainPage')
    return render(request, 'paginaCitacoes/main.html', {'user': request.session.get('user'), 'user_id': request.session.get('user_id'), 'citacoes':citacoes, 'numero_citacoes':len(citacoes)})

