from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from list.models import Avaliacao,Filmes,GeneroFilme,PlataformaStreamingFilme,SkinUser

def meta(req):
    return req.META.get('HTTP_REFERER', '/')


@login_required(login_url='/login/')
def createPostagem(req,pk):
    print('\n\n\nchegei\n\n\n',req,pk)

    context={}
    filme = Filmes.objects.get(id=pk)
    comentario = req.POST['comentario']
    nota = req.POST['nota']
    user =  SkinUser.objects.get(usuario__username=req.user)  
    try:
        ava = Avaliacao.objects.create(comentario=comentario, nota=nota, filme=filme, skin=user)
    except:
        context['error'] = 'Avaliação já foi feita'
    return postagem(req,pk,context)
    
def postagem(req,pk,context={}):
    filme = Filmes.objects.get(id=pk)     
    ava = Avaliacao.objects.filter(filme__id=pk)
    for a in ava:
        a.like_count = a.likes_dislikes.filter(vote=1).count()
        a.dislike_count = a.likes_dislikes.filter(vote=-1).count()
    generos = GeneroFilme.objects.filter(filme__id=pk)
    plataformas = PlataformaStreamingFilme.objects.filter(filme__id=pk)
    print(filme)
    print(ava)
    print(generos)
    print(plataformas)
    context.update({
        'filme': filme,
        'avaliacao': ava,
        'generos' : generos,
        'plataformas':plataformas
        }) 
   
    return render(req,'postagem.html',context)
