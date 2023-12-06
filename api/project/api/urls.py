from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api'

#ViewSets routers
router = DefaultRouter()
router.register('aluno', AlunoViewSet)
router.register('boletim', BoletimViewSet)
router.register('professor', ProfessorViewSet)
router.register('disciplina', DisciplinaViewSet)


#URLs view
urlpatterns = [
    
]

urlpatterns += router.urls