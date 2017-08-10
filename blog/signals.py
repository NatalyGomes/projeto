from django.db.models.signals import post_save
from django.dispatch import receiver

from.models import Aluno
from docxtpl import DocxTemplate
from blog import models
import os

@receiver(post_save, sender = models.Curso)
def documento(sender, instance, **kwargs):
    print "ficha.docx"
    doc = DocxTemplate("ficha1.docx")
    context = { 'Nome':instance.nome,
                'Coordenador':instance.coordenador
                }

@receiver(post_save, sender = models.Empresa)
def documento(sender, instance, **kwargs):
    print "ficha.docx"
    doc = DocxTemplate("ficha1.docx")
    context = { 'Nome':instance.nome,
                'Funcao_mercado_de_trabalho':instance.funcao_mercado_de_trabalho,
                'Nome_responsavel':instance.nome_responsavel,
                'Atividade':instance.atividade,
                'CPF_responsavel':instance.CPF_responsavel,
                'Email_supervisor':instance.email_supervisor,
                'CNPJ':instance.CNPJ,
                'Area_de_atuacao':instance.area_de_atuacao,
                'Endereco_empresa':instance.endereco_empresa,
                'Numero_empresa':instance.numero_empresa,
                'Bairro_empresa':instance.bairro_empresa,
                'Cidade_empresa':instance.cidade_empresa,
                'UF_empresa':instance.UF_empresa,
                'CEP_empresa':instance.CEP_empresa,
                'Telefone_empresa':instance.telefone_empresa,
                'Email_empresa':instance.email_empresa
                }

@receiver(post_save, sender = models.Aluno)
def documento(sender, instance, **kwargs):
    print "ficha.docx"
    doc = DocxTemplate("ficha1.docx")
    context = { 'Nome':instance.nome,
                'Nascimento':instance.nascimento,
                'Mae':instance.mae,
                'Pai':instance.pai,
                'CPF':instance.CPF,
                'RG':instance.RG,
                'Orgao_emissor':instance.orgao_emissor,
                'Local':instance.local,
                'Email':instance.email,
                'Curso':instance.curso.nome,
                'Matricula':instance.matricula,
                'Turma':instance.turma,
                'Turno':instance.turno,
                'Ano_de_conclusao':instance.ano_de_conclusao,
                'Telefone':instance.telefone,
                'Endereco':instance.endereco,
                'Bairro':instance.bairro,
                'Cidade':instance.cidade,
                'UF':instance.UF,
                'CEP':instance.CEP,
                'CNH':instance.CNH
                 }

@receiver(post_save, sender = models.Orientador)
def documento(sender, instance, **kwargs):
    print "ficha.docx"
    doc = DocxTemplate("ficha1.docx")
    context = { 'Nome':instance.nome,
                'Matricula_orientador':instance.matricula_orientador,
                'Email_orientador':instance.email_orientador
                }

@receiver(post_save, sender = models.Supervisor)
def documento(sender, instance, **kwargs):
    print "ficha.docx"
    doc = DocxTemplate("ficha1.docx")
    context = { 'Nome':instance.nome,
                'CPF_supervisor':instance.CPF_supervisor,
                'Email_supervisor':instance.email_supervisor,
                'Empresa':instance.empresa.nome,
                'Endereco_supervisor':instance.endereco_supervisor,
                'Bairro_supervisor':instance.bairro_supervisor,
                'Cidade_supervisor':instance.cidade_supervisor,
                'UF_supervisor':instance.UF_supervisor,
                'CEP_supervisor':instance.CEP_supervisor,
                'CREA':instance.CREA
                }

@receiver(post_save, sender = models.Estagio)
def documento(sender, instance, **kwargs):
    print "ficha.docx"
    doc = DocxTemplate("ficha1.docx")
    context = { 'Empresa':instance.empresa.nome,
                'Aluno':instance.aluno.nome,
                'Orientador':instance.orientador.nome,
                'Hr_inicial':instance.hr_inicial,
                'Hr_final':instance.hr_final,
                'Periodo_semanal':instance.periodo_semanal,
                'Dia_inicio':instance.dia_inicio,
                'Dia_fim':instance.dia_fim,
                'Duracao_minima':instance.duracao_minima,
                'Supervisor':instance.supervisor.nome,
                'Funcao':instance.funcao,
                'Local_do_estagio':instance.local_do_estagio
                }

    doc.render(context)
    doc.save("ficha1_editado.docx")
    
