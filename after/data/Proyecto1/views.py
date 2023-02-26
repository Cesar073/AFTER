from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context

def template1(request):
    
    mihtml = open(r"C:\Users\Ross\Desktop\data\Proyecto1\Proyecto1\plantillas\template1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = context()
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)


def hoy(request):
    dia = datetime.now()
    documentodetexto = f"Hoy es: {dia}"
    
    return HttpResponse(documentodetexto)
