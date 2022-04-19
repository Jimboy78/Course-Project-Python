#from msilib.schema import ListView
from django.shortcuts import redirect, render
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def Inicio (request): 
    return render(request, "Indice/Plantillas/index.html") 


class AboutUs (LoginRequiredMixin,TemplateView): 
    template_name = 'Indice/Plantillas/about_us.html'



class Blog (LoginRequiredMixin,TemplateView):
    template_name = 'Indice/Plantillas/blog.html'

    