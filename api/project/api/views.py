from api.serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import *


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer 

class BoletimViewSet(ModelViewSet):
    queryset = Boletim.objects.all()
    serializer_class = BoletimSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer