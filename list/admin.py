from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Filmes)
admin.site.register(models.Genero)
admin.site.register(models.GeneroFilme)
admin.site.register(models.PlataformaStreaming)
admin.site.register(models.PlataformaStreamingFilme)
admin.site.register(models.Playlist)
admin.site.register(models.PlaylistFilme)
admin.site.register(models.PlaylistUser)
admin.site.register(models.FilmesAssistidos)
admin.site.register(models.SkinUser)
admin.site.register(models.Avaliacao)
admin.site.register(models.Seguir)
admin.site.register(models.LikeDislike)