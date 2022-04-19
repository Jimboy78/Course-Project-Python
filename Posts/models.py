from django.db import models

# Create your models here.

class Post(models.Model):

    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)


