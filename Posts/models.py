from datetime import datetime

from django.db import models


# Create your models here.

class Post(models.Model):

    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


