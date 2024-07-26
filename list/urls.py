from django.urls import path
from . import views
from .pages.showMovieList import showMovieListURL
from .pages.login import loginURL
from .pages.playlist import playlistURL
from .pages.userprofile import urls
from .pages.avaliacao import urlavalicao
urlpatterns =[
    path("",views.index,name="index"),
    path("addFilme/",views.addFilme,name="addFilme"),
    path("removeFilme/<str:pk>",views.removeFilme,name="removeFilme"),
    path("editFilme/<str:pk>",views.editFilme,name="editFilme"),
    path('getMovieInfo/<str:pk>/', views.getMovieInfo, name='getMovieInfo'),
    path('seguindo/',views.avaliacaoSeguindo,name='avaliacaoSeguindo'),
    path('like/<int:ava_id>/', views.like_dislike, {'vote_type': 1}, name='like'),
    path('dislike/<int:ava_id>/', views.like_dislike, {'vote_type': -1}, name='dislike'),
    path('ava/<int:ava_id>/counts/', views.ava_counts, name='ava_counts'),
    
]

urlpatterns.extend(showMovieListURL.lista)
urlpatterns.extend(loginURL.lista)
urlpatterns.extend(playlistURL.lista)
urlpatterns.extend(urls.lista)
urlpatterns.extend(urlavalicao.lista)