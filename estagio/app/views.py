# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from . import models

def save_pdf(request, pk):
	curso = models.Curso.objects.get(pk=pk)
	print curso.nome
	return redirect('http://google.com/' + pk)