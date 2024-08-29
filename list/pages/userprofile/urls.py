from django.urls import path
from . import view
lista =[
    path("users/<str:pk>",view.userProfile,name="index"),
    path('addPlaylist/', view.addPlaylist, name='addPlaylist'),
    path('removePlaylist/<str:pk>/', view.removePlaylist, name='removePlaylist'),
    path('editPlaylist/<str:pk>/', view.editPlaylist, name='editPlaylist'),
    path('seguir/<int:pk>', view.seguir, name='seguir'),
    path('desseguir/<int:pk>',view.desseguir, name='desseguir')
]