from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_2(request):
    return HttpResponse(
        "<h1>Index de la App2</h1>")

def presentacion_2(request):
    html = """
    <p>Soy un parrafo de la App2.</p>
    <h2>Soy un subtitulo de la App2</h2>
"""
    return HttpResponse(html)


