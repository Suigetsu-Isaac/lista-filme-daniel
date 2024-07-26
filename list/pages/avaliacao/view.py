
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from list.models import PlataformaStreamingFilme,GeneroFilme, Avaliacao

def avaliacao(req,pk):

    if req.method == 'POST':
        pass
    else:
        ava = Avaliacao.objects.get(id = pk)
        plat = PlataformaStreamingFilme.objects.filter(filme__id = ava.filme.id)
        gen = GeneroFilme.objects.filter(filme__id = ava.filme.id)

        plat = plat.values_list('plataforma__nome')
        gen = gen.values_list('genero__nome')

        plat = [ p for p in plat][0]
        gen = [ g for g in gen][0]
      
        

        context={
            'id':ava.id,
            'filme':ava.filme,
            'user':ava.skin,
            'comentario': ava.comentario,
            'nota':ava.nota,
            'eu':req.user,
            'plataforma': plat,
            'genero': gen
            }
        return render(req,'avaliarFilme.html',context)
