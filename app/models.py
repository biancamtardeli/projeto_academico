from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Ocupações"

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return f'{self.nome} {self.UF}'
    

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()
    telefone = models.CharField(max_length=12)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Intituições"

    def __str__(self):
        return f'{self.nome} , {self.cidade}'


class Turno(models.Model):
    nome = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name_plural = "Turnos"

    def __str__(self):
        return self.nome
    

class Area(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.nome
    

class Turma(models.Model):
    nome = models.CharField(max_length=100, default='')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = "Turmas"

    def __str__(self):
        return self.nome
    

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default='')
    nome_do_pai = models.CharField(max_length=100, verbose_name="mãe", default='')
    nome_da_mae = models.CharField(max_length=100, verbose_name="pai", default='')
    cpf = models.CharField(max_length=11, default=0)
    data_nasc = models.DateField(default='2000-01-01', verbose_name="data de nascimento")
    email = models.URLField(default='')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default='')
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, default='')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return f'{self.nome} {self.ocupacao}'


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField(verbose_name="carga horária")
    duracao_meses = models.IntegerField(verbose_name="duração")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.nome} - {self.area_saber}'
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return f'{self.nome} - {self.area_saber}'
    

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField(default='2000-01-01', verbose_name="data de início")
    data_previsao_termino = models.DateField(default='2000-01-01', verbose_name="previsão de término")

    class Meta:
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return f'{self.pessoa}, {self.curso}, {self.instituicao}'
    

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

    class Meta:
        verbose_name_plural = "Frequências"

    def __str__(self):
        return f'{self.pessoa}, {self.disciplina}, {self.numero_faltas}'
    

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateField(default='2000-01-01')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
         verbose_name_plural = "Ocorrências"

    def __str__(self):
        return f'{self.descricao}, {self.pessoa}'


class TipoAvaliacao(models.Model):
    tipo_avaliacao = models.CharField(max_length=100, default='')

    class Meta:
         verbose_name_plural = "Tipos de Avaliação"

    def __str__(self):
        return self.tipo_avaliacao
    

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE, default='')


    class Meta:
         verbose_name_plural = "Avaliações"

    def __str__(self):
        return f'{self.descricao}, {self.nota}'
