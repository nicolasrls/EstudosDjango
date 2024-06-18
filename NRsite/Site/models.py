from django.db import models

# Create your models here.

class Lista(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    assunto = models.ForeignKey(Lista, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    