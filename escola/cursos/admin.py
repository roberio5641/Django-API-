from django.contrib import admin
from .models import Curso, Avaliacao

@admin.register(Curso)
class CursoAdimin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaoAdimin(admin.ModelAdmin):
    list_display = ('curso','nome','email','avaliacao','criacao','atualizacao','ativo')

