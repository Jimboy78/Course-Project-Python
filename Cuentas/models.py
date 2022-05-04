from django.db import models
from django.contrib.auth.models import User

class NuestroUser(models.Model):

    imagen = models.ImageField(upload_to='avatares', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, max_length=150)
    
    def __str__(self):
        return self.user.username