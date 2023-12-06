from django.contrib import admin
from .models import Aluno, Disciplina, Boletim, Professor
#from django.contrib.auth.admin import UserAdmin

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Boletim)
admin.site.register(Professor)