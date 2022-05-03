from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import  DetailView
from django.views.generic.edit import DeleteView
from .forms import Formulario_post,Buscar_post
from .models import Post
from Cuentas.views import Buscar_Url_Avatar


@login_required
def Formulario_posteo(request):
    if request.method == 'POST':
        form = Formulario_post(request.POST, files=request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            msj = form.cleaned_data['titulo']   
            posteo = Post(titulo=data ['titulo'], subtitulo=data['subtitulo'], texto=data['texto'], autor=data['autor'], imagen=data['imagen_post'])
            posteo.save()
            return render(request, "Indice/Plantillas/index.html", {'msj':f'Se creo el post "{msj}"', 'user_avatar':Buscar_Url_Avatar(request.user)})
        else:
            return render(request, "Posts/Plantillas/formulario_post.html", {'form':form, 'user_avatar':Buscar_Url_Avatar(request.user)})

    form = Formulario_post()
    return render(request, "Posts/Plantillas/formulario_post.html", {'form':form, 'user_avatar':Buscar_Url_Avatar(request.user)})


def Lista_post(request):
    buscar_post = request.GET.get('titulo',None)

    if buscar_post is not None:
        posts = Post.objects.filter(titulo__icontains=buscar_post)
    else:
        posts = Post.objects.all()
        
    form = Buscar_post()
    return render(request, "Posts/Plantillas/lista_posts.html", {'form':form,'posts':posts, 'user_avatar':Buscar_Url_Avatar(request.user)})


class Delete_post(DeleteView):
   model = Post
   template_name = 'Posts/Plantillas/Post_confirm_delete.html'
   success_url = reverse_lazy('Lista_posts')


class Detalle_post(DetailView):
    model = Post
    template_name = 'Posts/Plantillas/post_detail.html'
