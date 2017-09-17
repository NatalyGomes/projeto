# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

#admin.site.register(Curso)
admin.site.register(Empresa)
admin.site.register(Aluno)
admin.site.register(Orientador)
admin.site.register(Supervisor)
admin.site.register(Estagio)
admin.site.register(Fichas)
#admin.site.register(Ficha_Inscricao)
#admin.site.register(Ficha_Acompanhamento)
#admin.site.register(Ficha_Avaliacao_Estagio_Empresa)
#admin.site.register(Ficha_Avaliacao_Discente_Estagio)


from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

@admin.register (Curso)
class AccountAdmin( admin.ModelAdmin):
	list_display = (
		'nome',
		'coordenador',
		'accounts_actions',
		)

	def accounts_actions (self, obj):
		return format_html(
			'<a class = "button" href = "{}">Gerar PDF</a>',
			reverse('save_pdf', args=[obj.pk])
		)
		