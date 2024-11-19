from django.contrib import admin
from .models import *

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    model = Curso
    inlines = [DisciplinaInline]

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    model = Ocupacao
    inlines = [PessoaInline] 

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    model = Instituicao
    inlines = [CursoInline] 

class AreaAdmin(admin.ModelAdmin):
    model = Area
    inlines = [CursoInline] 

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    model = Disciplina
    inlines = [AvaliacaoInline] 

class TurmaAdmin(admin.ModelAdmin):
    model = Turma
    inlines = [PessoaInline] 


admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Matricula)
admin.site.register(Cidade)
admin.site.register(Ocorrencia)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Frequencia)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turno)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Pessoa)
admin.site.register(Avaliacao)
admin.site.register(TipoAvaliacao)