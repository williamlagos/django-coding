#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponseRedirect as redirect
from django.views.generic import ListView
from agenda.models import Paciente, Exame, Procedimento, Prescricao
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']


def footer(canvas, doc):
    canvas.saveState()
    P = Paragraph("Dr. Sérgio Eduardo Rocha - Ginecologista e Obstetrícia",styleN)
    w, h = P.wrap(doc.width, doc.bottomMargin)
    P.drawOn(canvas, doc.leftMargin, h)
    canvas.restoreState()


def pdfversion(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Impressao.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    pk = request.GET['pks']
    pres = Prescricao.objects.filter(pk=pk)
    if len(pres) > 0: 
        pr = pres[0]
        doc = BaseDocTemplate(response, pagesize=letter)
        frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
        template = PageTemplate(id='test', frames=frame, onPage=footer)
        doc.addPageTemplates([template])
        text = []
        text.append(Paragraph(pr.titulo,styleH))
        text.append(Paragraph(pr.descricao,styleN))
        doc.build(text)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def home(request):
    return redirect('admin/')


class RenovacaoView(ListView):
    model = Paciente
        # SELECT DISTINCTROW [Nome] & " " & [Sobrenome] AS NomeP, [Pacientes por Sobrenome].ID, [Endereco] & ", " & [Endnum] & " / " & [EndApart] AS EndP, [Pacientes por Sobrenome].CEP, [Pacientes por Sobrenome].Cidade, [Pacientes por Sobrenome].ID AS Cont, Procedimentos.Data
        # FROM [Pacientes por Sobrenome] INNER JOIN Procedimentos ON [Pacientes por Sobrenome].ID = Procedimentos.[ID da Paciente]
        # WHERE (((Aviso_renovar([Data],[Renovar]))=1))
        # ORDER BY [Nome] & " " & [Sobrenome]`
        # WITH OWNERACCESS OPTION;


class ObstetricoView(ListView):
    model = Exame
        # SELECT DISTINCTROW Obstetrico.*, [Exames Obstetricos].*, pacientes.Rubeola, pacientes.GS, pacientes.RH, pacientes.Gesta, pacientes.Para, Calc_Idade([Nasc]) AS Idade, [Nome] & " " & [Sobrenome] AS PNome, Obstetrico.ID AS Flt_IDObst
        # FROM pacientes INNER JOIN (Obstetrico INNER JOIN [Exames Obstetricos] ON Obstetrico.ID = [Exames Obstetricos].[ID do Obstetrico]) ON pacientes.ID = Obstetrico.[ID da Paciente]
        # WITH OWNERACCESS OPTION;


class ProcedimentoView(ListView):
    model = Procedimento
        # SELECT DISTINCTROW Procedimentos.*
        # FROM Procedimentos
        # WHERE (((Procedimentos.[ID da Paciente])=RetFiltro_IDPaciente()))
        # ORDER BY Procedimentos.Data
        # WITH OWNERACCESS OPTION;
