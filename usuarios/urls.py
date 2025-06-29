
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('inicio', views.home_view, name='home'),
    path('faq/', views.faq_view, name='faq'),

]
