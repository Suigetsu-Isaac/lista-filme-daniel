from django.http import JsonResponse
from list.models import Filmes,PlaylistFilme,PlaylistUser,FilmesAssistidos,SkinUser
from django.shortcuts import redirect, render,get_object_or_404
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
def addFilmePlaylist(req,playUserId,filmeId):
    
    if req.method == 'GET':
        return JsonResponse({'suscess':False,'message':'Precisa ser por POST'})
    
    try:
        
        play = PlaylistUser.objects.get(id=playUserId)
    
        filme = Filmes.objects.get(id = filmeId)
    
        PlaylistFilme.objects.create(
            play = play,
            filme = filme,
        )
        return JsonResponse({'success': True})
    except (PlaylistUser.DoesNotExist, Filmes.DoesNotExist):
        return JsonResponse({'success': False, 'message': 'Playlist ou Filme não encontrado'})
    
    
def removeFilmeFromPlaylist(req,pk):
    playFilme = PlaylistFilme.objects.get(id=pk)
    playFilme.delete()
  
    
    return redirect(req.META.get('HTTP_REFERER', '/'))

def addFilmeAssistido(req,pk):
    filme = Filmes.objects.get(id=pk)
    user = SkinUser.objects.get(usuario_id=req.user.id)
    assistido = FilmesAssistidos(
        filme = filme,
        usuario = user
    )
    print(assistido)
    
    assistido.save()
    return redirect(req.META.get('HTTP_REFERER', '/'))


def removeFilmeAssistido(req,pk):
    skin = SkinUser.objects.get(usuario_id = req.user.id)
    assistido = FilmesAssistidos.objects.get(filme__id=pk,usuario=skin)
    print(assistido)
    assistido.delete()
    return redirect(req.META.get('HTTP_REFERER', '/'))

def search_movies(request):
    query = request.GET.get('query', '')
    playlist_id = request.GET.get('playlist_id', '')

    # Get the playlist and its associated movies
    playlist = get_object_or_404(PlaylistUser, id=playlist_id)
    playlist_movies = PlaylistFilme.objects.filter(play=playlist).values_list('filme_id', flat=True)

    # Filter movies that match the query and are not already in the playlist
    suggestions = Filmes.objects.filter(nome__icontains=query).exclude(id__in=playlist_movies)

    # Return the filtered movies as JSON
    results = list(suggestions.values('id', 'nome'))

    return JsonResponse(results, safe=False)