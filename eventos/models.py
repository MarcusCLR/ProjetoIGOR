from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Participacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_confirmacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} em {self.evento.nome}"