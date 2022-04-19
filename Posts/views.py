from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import Formulario_post
from .models import Post

@login_required
def Formulario_posteo(request):
    if request.method == 'POST':

        form = Formulario_post(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            msj = form.cleaned_data['titulo']   
            posteo = Post(titulo=data ['titulo'], subtitulo=data['subtitulo'], texto=data['texto'], autor=data['autor'])
            posteo.save()
            return render(request, "Indice/Plantillas/index.html", {'msj':f'Se creo el post "{msj}"'})
        else:
            return render(request, "Posts/Plantillas/formulario_post.html", {'form':form})

    form = Formulario_post()
    return render(request, "Posts/Plantillas/formulario_post.html", {'form':form})
   
