from dataclasses import fields
from rest_framework import serializers
from .models import Aluno, Boletim, Professor, Disciplina

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = '__all__'


class BoletimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boletim
        fields = '__all__'
class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'