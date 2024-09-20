from django.urls import path
from . import views

from .pages.login import loginURL
from .pages.playlist import playlistURL
from .pages.userprofile import urls

from .pages.postagem import postagem
urlpatterns =[
    path("",views.index,name="index"),
    path("addFilme/",views.addFilme,name="addFilme"),
    path("removeFilme/<str:pk>",views.removeFilme,name="removeFilme"),
    path("editFilme/<str:pk>",views.editFilme,name="editFilme"),
    path('getMovieInfo/<str:pk>/', views.getMovieInfo, name='getMovieInfo'),
    path('seguindo/',views.avaliacaoSeguindo,name='avaliacaoSeguindo'),
    path('like/<str:ava_id>/', views.like_dislike, {'vote_type': 1}, name='like'),
    path('dislike/<str:ava_id>/', views.like_dislike, {'vote_type': -1}, name='dislike'),
    path('ava/<str:ava_id>/counts/', views.ava_counts, name='ava_counts'),
    path('navbar',views.navbar,name='navbar')
]


urlpatterns.extend(loginURL.lista)
urlpatterns.extend(playlistURL.lista)
urlpatterns.extend(urls.lista)

urlpatterns.extend(postagem.lista)