from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
      ocupacoes = Ocupacao.objects.all()
      return render(request, 'index.html', {'ocupacoes': ocupacoes})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      matriculas = Matricula.objects.all()
      return render(request, 'index.html', {'matriculas': matriculas})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      cidades = Cidade.objects.all()
      return render(request, 'index.html', {'cidades': cidades})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      ocorrencias = Ocorrencia.objects.all()
      return render(request, 'index.html', {'ocorrencias': ocorrencias})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      instituicoes = Instituicao.objects.all()
      return render(request, 'index.html', {'instituicoes': instituicoes})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      frequencias = Frequencia.objects.all()
      return render(request, 'index.html', {'frequencias': frequencias})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      turmas = Turma.objects.all()
      return render(request, 'index.html', {'turmas': turmas})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      areas = Area.objects.all()
      return render(request, 'index.html', {'areas': areas})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      cursos = Curso.objects.all()
      return render(request, 'index.html', {'cursos': cursos})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      turnos = Turno.objects.all()
      return render(request, 'index.html', {'turnos': turnos})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      disciplinas = Disciplina.objects.all()
      return render(request, 'index.html', {'disciplinas': disciplinas})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      matriculas = Matricula.objects.all()
      return render(request, 'index.html', {'matriculas': matriculas})
    def post(self, request):
       pass

class IndexView(View):
    def get(self, request):
      pessoas = Pessoa.objects.all()
      return render(request, 'index.html', {'pessoas': pessoas})
    def post(self, request):
       pass
    
class IndexView(View):
    def get(self, request):
      avaliacoes = Avaliacao.objects.all()
      return render(request, 'index.html', {'avaliacoes': avaliacoes})
    def post(self, request):
       pass