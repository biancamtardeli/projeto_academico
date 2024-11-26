from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
      page = "index.html"
      context = {
        "ocupacoes": Ocupacao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class OcupacaoView(View):
    def get(self, request):
      page = "ocupacao.html"
      context = {
        "ocupacoes": Ocupacao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class UfView(View):
    def get(self, request):
      page = "uf.html"
      context = {
        "ufs": UF.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class MatriculaView(View):
    def get(self, request):
      page = "matricula.html"
      context = {
        "matriculas": Matricula.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class CidadeView(View):
    def get(self, request):
      page = "cidade.html"
      context = {
        "cidades": Cidade.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
      
class OcorrenciaView(View):
    def get(self, request):
      page = "ocorrencia.html"
      context = {
        "ocorrencias": Ocorrencia.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class InstituicaoView(View):
    def get(self, request):
      page = "instituicao.html"
      context = {
        "instituicoes": Instituicao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class FrequenciaView(View):
    def get(self, request):
      page = "frequencia.html"
      context = {
        "frequencias": Frequencia.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class TurmaView(View):
    def get(self, request):
      page = "turma.html"
      context = {
        "turmas": Turma.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class AreaView(View):
    def get(self, request):
      page = "area.html"
      context = {
        "areas": Area.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class CursoView(View):
    def get(self, request):
      page = "curso.html"
      context = {
        "cursos": Curso.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class TurnoView(View):
    def get(self, request):
      page = "turno.html"
      context = {
        "turnos": Turno.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class DisciplinaView(View):
    def get(self, request):
      page = "disciplina.html"
      context = {
        "disciplinas": Disciplina.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass

class PessoaView(View):
    def get(self, request):
      page = "pessoa.html"
      context = {
        "pessoas": Pessoa.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class AvaliacaoView(View):
    def get(self, request):
      page = "avaliacao.html"
      context = {
        "avaliacoes": Avaliacao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class AlunoView(View):
    def get(self, request):
      page = "alunos.html"
      context = {
        "alunos": Aluno.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class FuncionarioView(View):
    def get(self, request):
      page = "funcionario.html"
      context = {
        "funcionarios": Funcionario.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass
    
class TipoAvaliacaoView(View):
    def get(self, request):
      page = "tipo_avaliacao.html"
      context = {
        "tipos_avaliacao": TipoAvaliacao.objects.all()
      }
      return render(request, page, context)
    def post(self, request):
       pass