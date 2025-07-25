from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('novo/', views.criar_evento, name='criar_evento'),
    path('sobre/', views.sobre, name='sobre'),
    path('criar_evento/', views.criar_evento, name='criar_evento'),
]
