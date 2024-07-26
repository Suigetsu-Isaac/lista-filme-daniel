from django.urls import path
from . import showMovieList as views

lista = [
    path('getMovieInfoComplete/<str:pk>/', views.getMovieInfoComplete, name='getMovieInfoComplete'),
    path('addGeneroToFilme/<str:pk>/', views.addGeneroToFilme, name='addGeneroToFilme'),
    path('addPlataformaToFilme/<str:pk>/', views.addPlataformaToFilme, name='addPlataformaToFilme'), 
    path('removeGeneroFromFilme/<str:pk>/', views.removeGeneroFromFilme, name='removeGeneroFromFilme'),
    path('removePlataformaFromFilme/<str:pk>/', views.removePlataformaFromFilme, name='removePlataformaFromFilme'),
]
