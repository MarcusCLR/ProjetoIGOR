from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import login_required

def listar_eventos(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

@login_required  # <-- adicione aqui na sua view completa
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})