from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    disciplinas = models.ManyToManyField(Disciplina, null=True)

    def __str__(self):
        return self.nome

class Boletim(models.Model):
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aluno.nome} / {self.disciplina.nome}"

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField(Disciplina, null=True)

    def __str__(self):
        return self.nome
    