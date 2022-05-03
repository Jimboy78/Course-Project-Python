from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cuentas.views import Buscar_Url_Avatar
from Posts.models import Post


def Inicio (request): 
    if request.user.is_authenticated:
        return render(request, "Indice/Plantillas/index.html",{'user_avatar':Buscar_Url_Avatar(request.user)}) 
    else:
        return render(request, "Indice/Plantillas/index.html")

@login_required
def AboutUs (request): 
    return render (request,'Indice/Plantillas/about_us.html',{'user_avatar':Buscar_Url_Avatar(request.user)})


@login_required
def Blog (request):
    posts = Post.objects.all()
    return render(request, "Indice/Plantillas/blog.html",{'posts': posts, 'user_avatar':Buscar_Url_Avatar(request.user)}) 
