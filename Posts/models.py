from datetime import date
from django.db import models
class Post(models.Model):

    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_posts', null=True, blank=True)
    fecha = models.DateField(default=date.today)
    

    def __str__(self):
        return self.titulo


