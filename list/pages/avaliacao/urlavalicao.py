from django.urls import path
from . import view
lista =[
    path("avaliacao/<str:pk>",view.avaliacao,name="index"),
]