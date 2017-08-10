from django.db import models
from django.utils import timezone
from django.contrib import admin

class Curso(models.Model):
    nome = models.CharField('nome',max_length = 50)
    coordenador = models.CharField('coordenador',max_length = 100)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField('nome',max_length = 200)
    funcao_mercado_de_trabalho = models.CharField('funcao_mercado_de_trabalho',max_length = 50)
    nome_responsavel = models.CharField('nome_responsavel',max_length = 100)
    atividade = models.CharField('atividade',max_length = 30)
    CPF_responsavel = models.CharField('CPF_responsavel',max_length = 11)
    email_supervisor = models.CharField('email_supervisor',max_length = 30)
    CNPJ = models.CharField('CNPJ',max_length = 18)
    area_de_atuacao = models.CharField('area_de_atuacao',max_length = 50)
    endereco = models.CharField('endereco',max_length = 100)
    numero = models.IntegerField()
    bairro = models.CharField('bairro',max_length = 50)
    cidade = models.CharField('cidade',max_length = 50)
    UF = models.CharField('UF',max_length = 2)
    CEP = models.CharField('CEP',max_length = 10)
    telefone = models.CharField('telefone',max_length = 20)
    email = models.CharField('email',max_length = 30)


    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField('nome',max_length = 100)
    nascimento = models.CharField('nascimento',max_length = 10)
    mae = models.CharField('mae',max_length = 100)
    pai = models.CharField('pai',max_length = 100)
    CPF = models.CharField('CPF',max_length = 11)
    RG = models.CharField('RG',max_length = 10)
    orgao_emissor = models.CharField('orgao_emissor',max_length = 10)
    local = models.CharField('local',max_length = 2)
    email = models.CharField('email',max_length = 50)
    curso = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Aluno', blank = True, null = True)
    matricula = models.CharField('matricula',max_length = 15)
    turma = models.CharField('turma',max_length = 10)
    turno = models.CharField('turno',max_length = 15)
    ano_de_conclusao = models.IntegerField()
    telefone = models.CharField('telefone',max_length = 20)
    endereco = models.CharField('endereco',max_length = 100)
    bairro = models.CharField('bairro',max_length = 50)
    cidade = models.CharField('cidade',max_length = 50)
    UF = models.CharField('UF',max_length = 2)
    CEP = models.CharField('CEP',max_length = 10)
    CNH = models.CharField('CNH',max_length = 2, blank = True, null = True)

    def __str__(self):
        return self.nome

class Orientador(models.Model):
    nome = models.CharField('nome',max_length = 100)
    matricula = models.CharField('matricula',max_length = 15)
    email = models.CharField('email',max_length = 30)

    def __str__(self):
        return self.nome

class Supervisor(models.Model):

    nome = models.CharField('nome',max_length = 100)
    CPF = models.CharField('CPF',max_length = 11)
    email = models.CharField('email',max_length = 30)
    empresa = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Supervisor')
    endereco = models.CharField('endereco',max_length = 50)
    bairro = models.CharField('bairro',max_length = 50)
    cidade = models.CharField('cidade',max_length = 50)
    UF = models.CharField('UF',max_length = 2)
    CEP = models.CharField('CEP',max_length = 10)
    CREA = models.CharField('CREA',max_length = 10)

    def __str__(self):
        return self.nome

class Estagio(models.Model):
    empresa = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Estagio')
    aluno = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Estagio')
    orientador = models.ForeignKey(Orientador, verbose_name = 'Orientador', related_name = 'Estagio')
    hr_inicial = models.CharField('hr_inicial',max_length = 5)
    hr_final = models.CharField('hr_final',max_length = 5)
    periodo_semanal = models.CharField('periodo_semanal',max_length = 30)
    dia_inicio = models.CharField('dia_inicio',max_length = 10)
    dia_fim = models.CharField('dia_fim',max_length = 10)
    duracao_minima = models.CharField('duracao_minima',max_length = 10)
    supervisor = models.ForeignKey(Supervisor, verbose_name = 'Supervisor', related_name = 'Estagio')
    funcao = models.CharField('funcao',max_length = 30)
    local_do_estagio = models.CharField('local_do_estagio',max_length = 30)

    def __str__(self):
        return '%s-%s' %(self.aluno.nome,self.orientador.nome)



#class Ficha_Acompanhamento(models.Model):
#    curso = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Acompanhamento')
#    professor = models.ForeignKey(Professor, verbose_name = 'Professor', related_name = 'Ficha_Acompanhamento')
#    aluno = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Acompanhamento')
#    empresa = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Ficha_Acompanhamento')

#    def __str__(self):
#        return '%s-%s-%s-%s' %(self.aluno.nome,self.curso.nome,self.empresa.nome,self.professor.name)

#class Plano_Estagio(models.Model):
#    aluno = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Plano_Estagio')
#    empresa = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Plano_Estagio')
#    professor = models.ForeignKey(Professor, verbose_name = 'Professor', related_name = 'Plano_Estagio')

#    def __str__(self):
#        return '%s-%s-%s' %(self.aluno.nome,self.professor.nome,self.empresa.nome)

#class Ficha_Inscricao(models.Model):
#    curso = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Inscricao')
#    aluno = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Inscricao')

#    def __str__(self):
#        return '%s-%s' %(self.aluno.nome,self.curso.nome)

#class Ficha_Avaliacao_Discente_Estagio(models.Model):
#    aluno = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Avaliacao_Discente_Estagio')
#    curso = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Avaliacao_Discente_Estagio')
#    empresa = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Ficha_Avaliacao_Discente_Estagio')

#    def __str__(self):
#        return '%s-%s-%s' %(self.aluno.nome,self.curso.nome,self.empresa.nome)

#class Ficha_Avaliacao_Estagio_Empresa(models.Model):
#    aluno = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Avaliacao_Estagio_Empresa')
#    curso = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Avaliacao_Estagio_Empresa')
#    empresa = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Ficha_Avaliacao_Estagio_Empresa')

#    def __str__(self):
#        return '%s-%s-%s' %(self.aluno.nome,self.curso.nome,self.empresa.nome)
