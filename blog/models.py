from django.db import models
from django.utils import timezone
from django.contrib import admin

class Curso(models.Model):
    nome = models.CharField('nome',max_length = 50)
    coordenador = models.CharField('coordenador',max_length = 100)
    testing = models.IntegerField('id', primary_key = True, default = '')

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField('nome',max_length = 200)
    atividade = models.CharField('atividade',max_length = 30)
    CNPJ = models.CharField('CNPJ',max_length = 18)
    area_de_atuacao = models.CharField('area_de_atuacao',max_length = 50)
    endereco = models.CharField('endereco',max_length = 100)
    bairro = models.CharField('bairro',max_length = 50)
    cidade = models.CharField('cidade',max_length = 50)
    UF = models.CharField('UF',max_length = 2)
    CEP = models.CharField('CEP',max_length = 10)
    telefone = models.CharField('telefone',max_length = 20)
    correio_eletronico = models.CharField('correio_eletronico',max_length = 50)
    responsavel = models.CharField('responsavel',max_length = 100)
    funcao = models.CharField('funcao',max_length = 30)
    local_do_estagio = models.CharField('local_do_estagio',max_length = 30)
    secao_departamento = models.CharField('secao_departamento',max_length = 30)
    supervisor_estagio = models.CharField('supervisor_estagio',max_length = 100)
    setor_estagio = models.CharField('setor_estagio',max_length = 30)
    regime_trabalho = models.CharField('regime_trabalho',max_length = 1)

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
    cursoFK = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Aluno')
    matricula = models.CharField('matricula',max_length = 15)
    turma = models.CharField('turma',max_length = 10)
    turno = models.CharField('turno',max_length = 15)
    ano_de_conclusao = models.IntegerField()
    correio_eletronico = models.CharField('correio_eletronico',max_length = 50)
    telefone = models.CharField('telefone',max_length = 20)
    endereco = models.CharField('endereco',max_length = 100)
    bairro = models.CharField('bairro',max_length = 50)
    cidade = models.CharField('cidade',max_length = 50)
    UF = models.CharField('UF',max_length = 2)
    CEP = models.CharField('CEP',max_length = 10)
    CNH = models.CharField('CNH',max_length = 2)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField('nome',max_length = 100)
    matricula = models.CharField('matricula',max_length = 15)
    correio_eletronico = models.CharField('correio_eletronico',max_length = 50)

    def __str__(self):
        return self.nome

class Estagio(models.Model):
    alunoFK = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Estagio')
    professorFK = models.ForeignKey(Professor, verbose_name = 'Professor', related_name = 'Estagio')
    horario_inicial = models.CharField('horario_inicial',max_length = 5)
    horario_final = models.CharField('horario_final',max_length = 5)
    dia_inicio = models.CharField('dia_inicio',max_length = 10)
    dia_fim = models.CharField('dia_fim',max_length = 10)
    duracao_minima = models.CharField('duracao_minima',max_length = 10)

    def __str__(self):
        return '%s-%s' %(self.alunoFK.nome,self.professorFK.nome)

class Responsavel(models.Model):
    nome = models.CharField('nome',max_length = 100)
    empresa = models.CharField('empresa',max_length = 100)
    endereco = models.CharField('endereco',max_length = 50)
    registro_CREA = models.CharField('registro_CREA',max_length = 10)
    CEP = models.CharField('CEP',max_length = 10)
    cidade = models.CharField('cidade',max_length = 30)

    def __str__(self):
        return self.nome

class Ficha_Acompanhamento(models.Model):
    cursoFK = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Acompanhamento')
    professorFK = models.ForeignKey(Professor, verbose_name = 'Professor', related_name = 'Ficha_Acompanhamento')
    alunoFK = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Acompanhamento')
    empresaFK = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Ficha_Acompanhamento')

    def __str__(self):
        return '%s-%s-%s-%s' %(self.alunoFK.nome,self.cursoFK.nome,self.empresaFK.nome,self.professorFK.name)

class Plano_Estagio(models.Model):
    alunoFK = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Plano_Estagio')
    empresaFK = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Plano_Estagio')
    professorFK = models.ForeignKey(Professor, verbose_name = 'Professor', related_name = 'Plano_Estagio')

    def __str__(self):
        return '%s-%s-%s' %(self.alunoFK.nome,self.professorFK.nome,self.empresaFK.nome)

class Ficha_Inscricao(models.Model):
    cursoFK = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Inscricao')
    alunoFK = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Inscricao')

    def __str__(self):
        return '%s-%s' %(self.alunoFK.nome,self.cursoFK.nome)

class Ficha_Avaliacao_Discente_Estagio(models.Model):
    alunoFK = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Avaliacao_Discente_Estagio')
    cursoFK = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Avaliacao_Discente_Estagio')
    empresaFK = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Ficha_Avaliacao_Discente_Estagio')

    def __str__(self):
        return '%s-%s-%s' %(self.alunoFK.nome,self.cursoFK.nome,self.empresaFK.nome)

class Ficha_Avaliacao_Estagio_Empresa(models.Model):
    alunoFK = models.ForeignKey(Aluno, verbose_name = 'Aluno', related_name = 'Ficha_Avaliacao_Estagio_Empresa')
    cursoFK = models.ForeignKey(Curso, verbose_name = 'Curso', related_name = 'Ficha_Avaliacao_Estagio_Empresa')
    empresaFK = models.ForeignKey(Empresa, verbose_name = 'Empresa', related_name = 'Ficha_Avaliacao_Estagio_Empresa')

    def __str__(self):
        return '%s-%s-%s' %(self.alunoFK.nome,self.cursoFK.nome,self.empresaFK.nome)
