"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('alunos/', AlunoView.as_view(), name='aluno'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('uf/', UfView.as_view(), name='uf'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('area/', AreaView.as_view(), name='area'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('turno/', TurnoView.as_view(), name='turno'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('funcionario/', FuncionarioView.as_view(), name='funcionario'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('tipo_avaliacao/', TipoAvaliacaoView.as_view(), name='tipo_avaliacao')
]
