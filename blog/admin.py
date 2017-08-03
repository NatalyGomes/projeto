# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(Curso)
admin.site.register(Empresa)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Responsavel)
admin.site.register(Estagio)
admin.site.register(Ficha_Inscricao)
admin.site.register(Ficha_Acompanhamento)
admin.site.register(Ficha_Avaliacao_Estagio_Empresa)
admin.site.register(Ficha_Avaliacao_Discente_Estagio)
