from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm
from eventos.forms import EventoForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('/eventos/')  # ou use redirect('nome_da_view')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'usuarios/login.html')

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
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    return render(request, 'usuarios/home.html')

@login_required(login_url='login')
def faq_view(request):
   return render(request, 'usuarios/faq.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # ou alguma página de confirmação
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

@login_required(login_url='login')
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')  # substitua com sua URL real
    else:
        form = EventoForm()
    return render(request, 'criar_evento.html', {'form': form})


