from django.urls import path
from . import playlist as views

lista = [   
    path('addFilmePlaylist/<str:pk>/', views.addFilmePlaylist, name='addFilmePlaylist'),
    path('removeFilmeFromPlaylist/<str:pk>/', views.removeFilmeFromPlaylist, name='removeFilmeFromPlaylist'),
    path('getAllMoviesByPlayList/<str:pk>/', views.getAllMoviesByPlayList, name='getAllMoviesByPlayList'),
    path('filmeAssistido/<str:pk>/',views.addFilmeAssistido, name='assisti'),
    path('filmeDesassistido/<str:pk>/',views.removeFilmeAssistido, name='desassistido'), 
]