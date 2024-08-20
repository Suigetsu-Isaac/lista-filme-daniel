from list.models import Filmes,PlaylistFilme,PlaylistUser,FilmesAssistidos
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
    
def getAllMoviesByPlayList(req,pk):
    print(req.user)
    
    filmes = Filmes.objects.all()
    
    playlist = PlaylistFilme.objects.filter(play__id=pk)
    playuser = PlaylistUser.objects.get(id=pk)
    print(playlist)
    saida = []
    lista = playlist.values_list('filme__nome', flat=True)
    
    for f in filmes:
        if f.nome not in lista:
            saida.append(f)
    print(playlist.values_list('filme', flat=True))        
    print('saida: ',saida)
    
    context={'allMovies':saida,'playuser':playuser,'lista':lista,'playlist':playlist}
   
            
    return render(req,'playlist.html',context)

@login_required(login_url="/login/")
def addFilmePlaylist(req,pk):
    play = PlaylistUser.objects.get(id=pk)
    filmeId = req.POST['filme']
    filme = Filmes.objects.get(id = filmeId)
    
    novo = PlaylistFilme(
        play = play,
        filme = filme,
    )

    novo.save()
    return redirect(req.META.get('HTTP_REFERER', '/'))
def removeFilmeFromPlaylist(req,pk):
    playFilme = PlaylistFilme.objects.get(id=pk)
    playFilme.delete()
  
    
    return redirect(req.META.get('HTTP_REFERER', '/'))

def addFilmeAssistido(req,pk):
    filme = Filmes.objects.get(id=pk)
    user = User.objects.get(username=req.user)
    assistido = FilmesAssistidos(
        filme = filme,
        usuario = user
    )
    print(assistido)
    
    assistido.save()
    return redirect(req.META.get('HTTP_REFERER', '/'))


def removeFilmeAssistido(req,pk):
    assistido = FilmesAssistidos.objects.get(filme__id=pk,usuario__username=req.user)
    print(assistido)
    assistido.delete()
    return redirect(req.META.get('HTTP_REFERER', '/'))