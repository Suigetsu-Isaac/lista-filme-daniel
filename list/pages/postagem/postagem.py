from django.urls import path
from . import views
lista =[
    path("postagem/<str:pk>",views.postagem,name="postagem"),
    path("criarpostagem/<str:pk>",views.createPostagem,name='criarpostagem')
]