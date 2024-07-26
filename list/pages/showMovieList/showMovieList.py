from list.models import Genero, GeneroFilme, PlataformaStreaming, PlataformaStreamingFilme, Filmes
from django.shortcuts import redirect, render

def getMovieInfoComplete(req,pk):
    filme = Filmes.objects.get(id = pk)
    list_genero_filme = GeneroFilme.objects.filter(filme__id = pk)
    generos = Genero.objects.all()
    plataformas = PlataformaStreaming.objects.all()
    list_plataforma_filme = PlataformaStreamingFilme.objects.filter(filme__id = pk)
    saida = []
    saida_plataforma = []
    print(generos)
    print(filme)
    print(plataformas)
    for g in generos:
        if g.nome not in list_genero_filme.values_list('genero__nome', flat=True):
            saida.append(g)
    for p in plataformas:
        if p.nome not in list_plataforma_filme.values_list('plataforma__nome', flat=True):
            saida_plataforma.append(p)
    print(saida)
    print(saida_plataforma)
    context = {
        'generos': saida,
        'filme': filme,
        'list_genero_filme': list_genero_filme,
        'plataformas': saida_plataforma,
        'list_plataforma_filme':list_plataforma_filme  
    }
    return render(req,'showMovieList.html',context)
def addGeneroToFilme(req,pk):
    filme = Filmes.objects.get(id = pk)
    generoId = req.POST['genero']
    genero = Genero.objects.get(id = int(generoId))
    
    novoGeneroFilme = GeneroFilme(
        filme = filme,
        genero = genero
    )
    novoGeneroFilme.save()
    return redirect(req.META.get('HTTP_REFERER', '/'))


def addPlataformaToFilme(req,pk):
    filme = Filmes.objects.get(id = pk)

    plataformaId = req.POST['plataforma']
    plataforma = PlataformaStreaming.objects.get(id = int(plataformaId))
    
    novaPlataformaFilme = PlataformaStreamingFilme(
        filme = filme,
        plataforma = plataforma
    )
    novaPlataformaFilme.save()
    return redirect(req.META.get('HTTP_REFERER', '/'))

def removeGeneroFromFilme(req,pk):
    genFilme=GeneroFilme.objects.get(id=pk)
    genFilme.delete()
    return redirect(req.META.get('HTTP_REFERER', '/'))

def removePlataformaFromFilme(req,pk):
    platFilme=PlataformaStreamingFilme.objects.get(id=pk)
    platFilme.delete()
    return redirect(req.META.get('HTTP_REFERER', '/'))