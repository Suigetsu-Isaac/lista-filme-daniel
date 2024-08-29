from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from list.models import  SkinUser,PlaylistUser,Playlist,Seguir,FilmesAssistidos
from django.template.defaulttags import register

def meta(req):
    return req.META.get('HTTP_REFERER', '/')

def userProfile(req,pk):
    
    if req.method == 'POST':
        
        return postProfile(req,pk)
    else:
     print('pk:',pk)
     user = SkinUser.objects.get(id=pk)
     play = PlaylistUser.objects.filter(user__id = user.usuario.id)    
     skin = SkinUser.objects.get(id=pk)
     print('playlist: ',play)

     skins = SkinUser.objects.all()
     
     
     assistido = FilmesAssistidos.objects.filter(usuario__id=pk)
     print('assistido ',assistido) 

     
     seguindo = user.seguindo.values_list('followed', flat=True)
     seguir = skins.exclude(id__in=seguindo).exclude(id=user.id)


     seguindo_ids = set(user.seguindo.values_list('followed_id', flat=True))   

     print('seguir',seguir)

     context = {'user':skin.usuario,
                'skin':skin,
                'can_edit':False,
                'playlist':play,
                'seguindo':user.seguindo.all(),
                'seguidores':user.seguidores.all(),
                'skins':skins,
                'seguir':seguir,
                'seguindo_ids':seguindo_ids,
                'assistido':assistido,}
        
     if skin.usuario.pk == req.user.pk:
         context['can_edit'] = True    
    
     return render(req,'userprofile.html',context)
    

def postProfile(req,pk):
    avatar = req.FILES.get('avatar')
    print(pk)
    skin = SkinUser (
        id = pk,
        img = avatar,
        usuario = req.user
    )
    print(skin)
    skin.save()
    print(skin.img)
    print(type(skin.img))
    print(pk)
    return redirect(meta(req))

def addPlaylist(req):
    user = User.objects.get(id=req.user.id)
    nome = req.POST['nome']
    desc = req.POST['desc']
    
    novo = Playlist(
        nome = nome,
        desc = desc
    )
    novo.save()
    
    associacao = PlaylistUser(
        user = user,
        play = novo
    )
    
    print(f'\n\n playlist nome {novo.nome} \n playlist descricao: {novo.desc}\n')
    print(f'\n associacao usuario: {associacao.user}, associacao playlist: {associacao.play.id} ')
    
    associacao.save()    
    return redirect(meta(req))


def removePlaylist(req,pk):
    playuser = PlaylistUser.objects.get(id=pk)
    playlist = Playlist.objects.get(id=playuser.play.id)
    print(playuser.delete())
    print(playlist.delete())
    return redirect(meta(req))


def editPlaylist(req,pk):
    playlist = Playlist.objects.get(id=pk)
    nome = req.POST['nome']
    desc = req.POST['desc']
    playlist.nome = nome
    playlist.desc = desc
    
    playlist.save()
    return redirect(meta(req))


def seguir(req,pk):

    seguir = get_object_or_404(SkinUser, id=pk)
    eu = get_object_or_404(SkinUser,usuario__id=req.user.id)
    Seguir.objects.get_or_create(follower=eu, followed=seguir)
    return redirect(meta(req))
    
def desseguir(req,pk):
    desseguir = get_object_or_404(SkinUser, id=pk)
    eu = get_object_or_404(SkinUser,usuario__id=req.user.id)
    Seguir.objects.filter(follower=eu, followed=desseguir).delete()
    return redirect(meta(req))
