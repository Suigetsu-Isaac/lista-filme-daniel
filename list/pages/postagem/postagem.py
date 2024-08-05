from django.urls import path
from . import views
lista =[
    path("postagem/<str:pk>",views.postagem,name="postagem"),
]