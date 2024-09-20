from django.urls import path
from . import views
lista =[
    path("postagem/<str:pk>",views.postagem,name="postagem"),
    path("criarpostagem/<str:pk>",views.createPostagem,name='criarpostagem'),
    path("removerPostagem/<str:pk>",views.removerPostagem,name='removerPostagem'),
    path('editarPostagem/<str:pk>',views.editarPostagem,name='editarpostagem')
]