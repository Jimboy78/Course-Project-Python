from django.db import models
from django.contrib.auth.models import User

class NuestroUser(models.Model):

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #nombre = models.CharField(max_length=50)
    #apellido = models.CharField(max_length=50)
    #telefono = models.CharField(max_length=10)
    #direccion = models.CharField(max_length=50)
    #ciudad = models.CharField(max_length=50)
    #pais = models.CharField(max_length=50)
    #codigo_postal = models.CharField(max_length=10)
    #fecha_nacimiento = models.DateField()
    #fecha_registro = models.DateField(auto_now_add=True)
    #fecha_actualizacion = models.DateField(auto_now=True)
    #is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username