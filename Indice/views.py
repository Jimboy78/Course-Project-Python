#from msilib.schema import ListView
from urllib import request
from django.shortcuts import redirect, render
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from Posts.forms import Formulario_post
from Posts.models import Post

def Inicio (request): 
    return render(request, "Indice/Plantillas/index.html") 


class AboutUs (LoginRequiredMixin,TemplateView): 
    template_name = 'Indice/Plantillas/about_us.html'


@login_required
def Blog (request):
    posts = Post.objects.all()
    return render(request, "Indice/Plantillas/blog.html", {'posts': posts}) 
