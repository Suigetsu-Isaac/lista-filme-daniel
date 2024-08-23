from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
# Create your models here.
class Filmes(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    cover = models.ImageField(null=True, blank=True, upload_to='images/',default='/images/filme-default.png' )
    sinopse = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

    @property
    def count_avaliacoes(self):
        return self.avaliacoes.count()
    
    @property
    def media_notas(self):
        return self.avaliacoes.aggregate(Avg('nota'))['nota__avg']

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
    logo = models.ImageField(null=True, blank=True, upload_to='images/',default='/images/filme-default.png' )
    def __str__(self):
        return self.nome

class PlataformaStreamingFilme(models.Model):
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE)
    plataforma = models.ForeignKey(PlataformaStreaming,on_delete=models.CASCADE)
    urlFilme= models.CharField(max_length=100)
    def __str__(self):
        return self.filme.__str__()+" - "+self.plataforma.__str__()+' se encontra em: '+self.urlFilme


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


class SkinUser(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to='images/',default='/images/profile-default.png')
    bio = models.CharField(max_length=255, default=f"Olá gosto de variados generos de filmes e quero conhecer novos amigos")
    
    def __str__(self):
        return f'{self.usuario} - {self.img.name} in {self.img.url}'



    
class FilmesAssistidos(models.Model):
    usuario = models.ForeignKey(SkinUser,on_delete=models.CASCADE)    
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.usuario.__str__()+" - "+self.filme.__str__()

    class Meta:
        unique_together = ('usuario', 'filme')



class Avaliacao(models.Model):
    comentario = models.CharField(max_length=255)
    nota = models.IntegerField() 
    filme = models.ForeignKey(Filmes,on_delete=models.CASCADE,related_name='avaliacoes')
    skin = models.ForeignKey(SkinUser,on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        print(self.skin)
        return f"nota: {self.nota} - {self.comentario} de {self.filme.nome} por {self.skin}"
    
    class Meta:
        unique_together = ('filme', 'skin')

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
    follower = models.ForeignKey(SkinUser, related_name='seguindo' ,on_delete=models.CASCADE)
    followed = models.ForeignKey(SkinUser, related_name='seguidores' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('follower', 'followed')
    
    def __str__(self):
        return f'{self.follower} está seguindo {self.followed}' 

