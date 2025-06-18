from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Página de login")

def signup_view(request):
    return render(request, 'usuarios/signup.html')

def logout_view(request):
    return HttpResponse("Logout feito")
