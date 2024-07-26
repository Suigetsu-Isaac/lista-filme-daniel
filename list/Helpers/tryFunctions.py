from list.models import Filmes, Playlist,PlaylistUser, SkinUser

def trySkin(pk):
    try:
        return SkinUser.objects.get(usuario__id=pk)
    except:
        return None