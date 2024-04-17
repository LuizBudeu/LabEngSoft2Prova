from django.db import models

# Create your models here.
# class Usuario(models.Model):
#     nome = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Estadio(models.Model):
#     nome = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Vaga(models.Model):
#     estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Ingresso(models.Model):
    STATUS_CHOICES = [
            (0, 'Disponível'),
            (1, 'Reservado'),
            (2, 'Cancelado')
        ]

    nome_usuario = models.CharField(max_length=200, null=True, blank=True)
    nome_estadio = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




