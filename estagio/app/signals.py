from django.db.models.signals import post_save
from django.dispatch import receiver


from docxtpl import DocxTemplate
from app import models
import os

#@receiver(post_save, sender = models.Curso)
#def documento(sender, instance, **kwargs):
#    print "ficha.docx"
#    doc = DocxTemplate("..............")
#    context = { 'Nome':instance.nome,
#                'Coordenador':instance.coordenador
#               }


#   doc.render(context)
#    doc.save("............")




#@receiver(post_save, sender = models.Empresa)
#def documento(sender, instance, **kwargs):
#  print "ficha.docx"
#    doc = DocxTemplate(..............)

#   context = { 'Nome':instance.nome,
#                'Funcao_mercado_de_trabalho':instance.funcao_mercado_de_trabalho,
#                'Nome_responsavel':instance.nome_responsavel,
#                'Atividade':instance.atividade,
#                'CPF_responsavel':instance.CPF_responsavel,
#                'Email_supervisor':instance.email_supervisor,
#                'CNPJ':instance.CNPJ,
#                'Area_de_atuacao':instance.area_de_atuacao,
#               'Endereco_empresa':instance.endereco_empresa,
#               'Numero_empresa':instance.numero_empresa,
#              'Bairro_empresa':instance.bairro_empresa,
#             'Cidade_empresa':instance.cidade_empresa,
#            'UF_empresa':instance.UF_empresa,
#              'CEP_empresa':instance.CEP_empresa,
#                'Telefone_empresa':instance.telefone_empresa,
#                'Email_empresa':instance.email_empresa
#                }

#    doc.render(context)
#    doc.save(".....................")




#@receiver(post_save, sender = models.Aluno)
#def documento(sender, instance, **kwargs):
    #print "ficha.docx"
    #doc = DocxTemplate(".................")
    #context = { 'Nome':instance.nome,
                #'Nascimento':instance.nascimento,
                #'Mae':instance.mae,
                #'Pai':instance.pai,
                #'CPF':instance.CPF,
                #'RG':instance.RG,
                #'Orgao_emissor':instance.orgao_emissor,
                #'Local':instance.local,
                #'Email':instance.email,
                #'Curso':instance.curso.nome,
                #'Matricula':instance.matricula,
                #'Turma':instance.turma,
                #'Turno':instance.turno,
                #'Ano_de_conclusao':instance.ano_de_conclusao,
                #'Telefone':instance.telefone,
                #'Endereco':instance.endereco,
                #'Bairro':instance.bairro,
                #'Cidade':instance.cidade,
                #'UF':instance.UF,
                #'CEP':instance.CEP,
                #'CNH':instance.CNH
                 #}
#
#

#
    #doc.render(context)
    #doc.save(".....................")
#
#
#
#
#@receiver(post_save, sender = models.Orientador)
#def documento(sender, instance, **kwargs):
    #print "ficha.docx"
    #doc = DocxTemplate(".................")
    #context = { 'Nome':instance.nome,
                #'Matricula_orientador':instance.matricula_orientador,
                #'Email_orientador':instance.email_orientador
                #}
#
    #doc.render(context)
    #doc.save(".....................")
#
#
#
#
#
#
#
#
#@receiver(post_save, sender = models.Supervisor)
#def documento(sender, instance, **kwargs):
    #print "ficha.docx"
    #doc = DocxTemplate(".....................")
    #context = { 'Nome':instance.nome,
                #'CPF_supervisor':instance.CPF_supervisor,
                #'Email_supervisor':instance.email_supervisor,
                #'Empresa':instance.empresa.nome,
                #'Endereco_supervisor':instance.endereco_supervisor,
                #'Bairro_supervisor':instance.bairro_supervisor,
                #'Cidade_supervisor':instance.cidade_supervisor,
                #'UF_supervisor':instance.UF_supervisor,
                #'CEP_supervisor':instance.CEP_supervisor,
                #'CREA':instance.CREA,
                #}
#
    #doc.render(context)
    #doc.save(".....................")










@receiver(post_save, sender = models.Estagio)
def documento(sender, instance, **kwargs):
    
    

    context = {
                #curso
                'Nome_curso': instance.curso.nome,
                'curso_coordenador' :instance.curso.coordenador,
                



                #empresa
                'Empresa':instance.empresa.nome,
                'Funcao_mercado_de_trabalho':instance.empresa.funcao_mercado_de_trabalho,
                'Nome_responsavel_empresa':instance.empresa.nome_responsavel,
                'Atividade':instance.empresa.atividade,
                'CPF_responsavel':instance.empresa.CPF_responsavel,
                'Email_supervisor':instance.empresa.email_supervisor,
                'CNPJ':instance.empresa.CNPJ,
                'Area_de_atuacao':instance.empresa.area_de_atuacao,
                'Endereco_empresa':instance.empresa.endereco,
                'Numero_empresa':instance.empresa.numero,
                'Bairro_empresa':instance.empresa.bairro,
                'Cidade_empresa':instance.empresa.cidade,
                'UF_empresa':instance.empresa.UF,
                'CEP_empresa':instance.empresa.CEP,
                'Telefone_empresa':instance.empresa.telefone,
                'Email_empresa':instance.empresa.email,

                #Aluno
                'Nome_aluno':instance.aluno.nome,
                'Nascimento':instance.aluno.nascimento,
                'Mae':instance.aluno.mae,
                'Pai':instance.aluno.pai,
                'CPF':instance.aluno.CPF,
                'RG':instance.aluno.RG,
                'Orgao_emissor':instance.aluno.orgao_emissor,
                'Local':instance.aluno.local,
                'Email':instance.aluno.email,
                'Curso':instance.aluno.curso.nome,
                'Matricula':instance.aluno.matricula,
                'Turma':instance.aluno.turma,
                'Turno':instance.aluno.turno,
                'Ano_de_conclusao':instance.aluno.ano_de_conclusao,
                'Telefone':instance.aluno.telefone,
                'Endereco':instance.aluno.endereco,
                'Bairro':instance.aluno.bairro,
                'Cidade':instance.aluno.cidade,
                'UF':instance.aluno.UF,
                'CEP':instance.aluno.CEP,
                'CNH':instance.aluno.CNH,


                #orientador
                'Nome_orientador':instance.orientador.nome,
                'Matricula_orientador':instance.orientador.matricula,
                'Email_orientador':instance.orientador.email,



                 #supervisor
                'Nome_supervisor':instance.supervisor.nome,
                'CPF_supervisor':instance.supervisor.CPF,
                'Email_supervisor':instance.supervisor.email,
                'Empresa':instance.supervisor.empresa.nome,
                'Endereco_supervisor':instance.supervisor.endereco,
                'Bairro_supervisor':instance.supervisor.bairro,
                'Cidade_supervisor':instance.supervisor.cidade,
                'UF_supervisor':instance.supervisor.UF,
                'CEP_supervisor':instance.supervisor.CEP,
                'CREA':instance.supervisor.CREA,


                
                
                #Estagio
                'Hr_inicial':instance.hr_inicial,
                'Hr_final':instance.hr_final,
                'Periodo_semanal':instance.periodo_semanal,
                'Dia_inicio':instance.dia_inicio,
                'Dia_fim':instance.dia_fim,
                'Duracao_minima':instance.duracao_minima,               
                'Funcao':instance.funcao,
                'Local_do_estagio':instance.local_do_estagio
                }



    print context

    doc = DocxTemplate(instance.fichas.modelo1)
    doc.render(context)
    doc.save("ficha1_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo2)
    doc.render(context)
    doc.save("ficha2_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo3)
    doc.render(context)
    doc.save("ficha3_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo4)
    doc.render(context)
    doc.save("ficha4_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo5)
    doc.render(context)
    doc.save("ficha5_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo6)
    doc.render(context)
    doc.save("ficha6_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo7)
    doc.render(context)
    doc.save("ficha7_editada.docx")
    

    doc = DocxTemplate(instance.fichas.modelo8)
    doc.render(context)
    doc.save("ficha2_editada.docx")
    






    os.system('unoconv ficha1_editada.docx')
    os.system('unoconv ficha2_editada.docx')
    os.system('unoconv ficha3_editada.docx')
    os.system('unoconv ficha4_editada.docx')
    os.system('unoconv ficha5_editada.docx')
    os.system('unoconv ficha6_editada.docx')
    os.system('unoconv ficha7_editada.docx')
    os.system('unoconv ficha8_editada.docx')