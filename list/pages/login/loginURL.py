from django.urls import path
from . import login as views

lista = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cad_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
]