from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    return HttpResponse("Página de login")

def signup_view(request):
    print("⚠️ Entrou na view de cadastro!")

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuário já está em uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/signup.html')


def logout_view(request):
    return HttpResponse("Logout feito")

def home_view(request):
    return render(request, 'usuarios/home.html')

