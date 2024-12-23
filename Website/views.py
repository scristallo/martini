from django.shortcuts import render
from .models import Tabella_immagini


# Create your views here.

def Website(request):
    immagini_sito =Tabella_immagini.objects.all()
    return render(request,'Website/homepagemartini.html', {'immagini_sito': immagini_sito})
