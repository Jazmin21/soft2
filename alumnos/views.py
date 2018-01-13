from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    personas = [
        { 'nombre' : 'Juanita', 'edad' : 20 },
        { 'nombre' : 'Pepito', 'edad' : 28 },
        { 'nombre' : 'Luisito', 'edad' : 10 }
    ]
    variables = {
        'lista_personas' : personas
    }
    return render(request, 'main.html', variables)
