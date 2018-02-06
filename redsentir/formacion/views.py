from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def guia(request,pid):
    return render(request, 'sitio/formacion/guia.html',{'prueba':20,})

@login_required
def modulo(request,pid):
    return render(request, 'sitio/formacion/modulo.html',{'prueba':20,})

@login_required
def jovenes(request):
    return render(request, 'sitio/formacion/jovenes.html')

@login_required
def docentes(request):
    return render(request, 'sitio/formacion/docentes.html')