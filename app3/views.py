from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index3(request):
    return HttpResponse(
        "<h1>Index de la App3</h1>")

def presentacion_3(request):
    html = """
    <p>Soy un parrafo de la App3.</p>
    <h2>Soy un subtitulo de la App3</h2>
"""
    return HttpResponse(html)