from django.db import models

# Create your models here.

class Tabella_immagini(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    descrizione = models.CharField(max_length=5000)

    def __str__(self):
        return self.nome