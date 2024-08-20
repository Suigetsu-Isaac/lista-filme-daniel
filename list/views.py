from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from list.models import Filmes,SkinUser,Avaliacao, Seguir,LikeDislike

def index(req,context={}):
   
    ava = Avaliacao.objects.all()
    
    filmes = Filmes.objects.all()
    context['filmes']=filmes
    allSkins = SkinUser.objects.all()
    print(ava)
    
    for a in ava:
        a.like_count = a.likes_dislikes.filter(vote=1).count()
        a.dislike_count = a.likes_dislikes.filter(vote=-1).count()

    print('\n\n\n ava',ava)
    avas = [a for a in ava]
    print('avas: ',avas) 

    try:
        myskin = SkinUser.objects.get(usuario__id = req.user.id)
        context['user'] = req.user
        context['myskin'] = myskin
    except:
        context['user'] = None

    
    print(context.get('ava'))
    if context.get('ava') is None:
        context['ava'] = avas
    

    skins = [a for a in allSkins if a.usuario.id != req.user.id]

    print('skins:',skins)
    
    context['skins'] = skins  
    return render(req,"index.html",context)


# Filmes   
def addFilme(req):
    nome=req.POST['nome']
    duracao=req.POST["duracao"]
    print(nome)
    novo = Filmes(
       nome=nome,duracao=duracao 
    )
    print(novo)
    novo.save()
    return redirect("index")

def removeFilme(req,pk):
    film=Filmes.objects.get(id=pk)
    film.delete()
    return redirect("index")


def editFilme(request,pk):
    film =Filmes.objects.get(id=pk)
    print(film)
    nome =request.POST["nome"]
    duracao=request.POST['duracao']
    film  = Filmes(
       id=pk,nome=nome,duracao=duracao 
    )
    print(film)
    film.save()
    return redirect('index')

def getMovieInfo(req,pk):
    filme = Filmes.objects.get(id = pk)
    
    
    novoFilme = {
        "filme": filme.nome,
        "duracao": filme.duracao,  
    }
    return JsonResponse(novoFilme)



def avaliacaoSeguindo(req):

    user =  User.objects.get(id=req.user.id)

    seguidos_ids = Seguir.objects.filter(follower=user).values_list('followed_id', flat=True)
    avas = Avaliacao.objects.filter(skin__usuario_id__in=seguidos_ids).select_related('skin__usuario')

    for a in avas:
        a.like_count = a.likes_dislikes.filter(vote=1).count()
        a.dislike_count = a.likes_dislikes.filter(vote=-1).count()
    print(f'\n avas: {avas} \n\n')
    context = {'ava':avas}


    return index(req,context)


def pegarSeguidores(req):
    user =  User.objects.get(id=req.user.id)
    seguindo =  user.seguindo.all()
    seguidores = user.seguidores.all()
    print('\n\n\nseguindo: ',seguindo)
    print('\n\n\nseguidores: ',seguidores)


def like_dislike(request, ava_id, vote_type):
    ava = get_object_or_404(Avaliacao, id=ava_id)
    print('\n\n\n ava em like / deslike \n\n\n',ava)
    user = request.user

    try:
        like_dislike = LikeDislike.objects.get(user=user, ava=ava)
        if like_dislike.vote == vote_type:
            like_dislike.delete()
            response = {'status': 'deleted'}
        else:
            like_dislike.vote = vote_type
            like_dislike.save()
            response = {'status': 'updated'}
    except LikeDislike.DoesNotExist:
        LikeDislike.objects.create(user=user, ava=ava, vote=vote_type)
        response = {'status': 'created'}
    return JsonResponse(response)

def ava_counts(request, ava_id):
    ava = get_object_or_404(Avaliacao, id=ava_id)
    likes = ava.likes_dislikes.filter(vote=1).count()
    dislikes = ava.likes_dislikes.filter(vote=-1).count()
    return JsonResponse({'likes': likes, 'dislikes': dislikes})

def navbar(req):
    
    try:
        myskin = SkinUser.objects.get(usuario__id=req.user.id)
        print('myskin',myskin)
        dic = {
            'id': myskin.id,
            'img': myskin.img.url,
            'user': myskin.usuario.username,
            'bio': myskin.bio
        }
        print('dic',dic)

        return JsonResponse(dic)
    except:
        
        return JsonResponse({'user':None})
    