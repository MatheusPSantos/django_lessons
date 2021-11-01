from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL_CHOICES = (('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado'))
    codigo_curso = models.CharField(max_length=10)
    descricao = models.TextField(max_length=120)
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
    