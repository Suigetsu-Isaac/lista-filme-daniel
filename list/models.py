from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Filmes(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    cover = models.ImageField(null=True, blank=True, upload_to='images/',default='/images/filme-default.png' )
    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class GeneroFilme(models.Model):
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    def __str__(self):
        return self.filme.__str__()+" - "+self.genero.__str__()
   
class PlataformaStreaming(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class PlataformaStreamingFilme(models.Model):
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE)
    plataforma = models.ForeignKey(PlataformaStreaming,on_delete=models.CASCADE)

    def __str__(self):
        return self.filme.__str__()+" - "+self.plataforma.__str__()

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome + "\n" + self.desc

class PlaylistUser(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    play = models.ForeignKey(Playlist, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.__str__() + ' - ' + self.play.__str__()

class PlaylistFilme(models.Model):
    play = models.ForeignKey(PlaylistUser,on_delete= models.CASCADE)
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.play.user.__str__()+": "+self.play.play.nome + ' - ' + self.filme.nome

           
    
class FilmesAssistidos(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)    
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.__str__()+" - "+self.filme.__str__()



class SkinUser(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to='images/',default='/images/profile-default.png')
    
    def __str__(self):
        return f'{self.usuario} - {self.img.name} in {self.img.url}'

   

class Avaliacao(models.Model):
    comentario = models.CharField(max_length=255)
    nota = models.IntegerField()  
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE,null=True)
    skin = models.ForeignKey(SkinUser,on_delete=models.CASCADE, null=True)

   
   
    def __str__(self):
        print(self.skin)
        return f"nota: {self.nota} - {self.comentario} de {self.filme} por {self.skin}"
    

class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTE_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ava = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='likes_dislikes')
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'ava')

class Seguir(models.Model):
    follower = models.ForeignKey(User, related_name='seguindo' ,on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='seguidores' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('follower', 'followed')
    
    def __str__(self):
        return f'{self.follower} está seguindo {self.followed}' 
