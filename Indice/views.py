from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cuentas.views import buscar_url_avatar
from Posts.models import Post


def inicio (request): 
    if request.user.is_authenticated:
        return render(request, "Indice/Plantillas/index.html",{'user_avatar':buscar_url_avatar(request.user)}) 
    else:
        return render(request, "Indice/Plantillas/index.html")

@login_required
def about_us (request): 
    return render (request,'Indice/Plantillas/about_us.html',{'user_avatar':buscar_url_avatar(request.user)})


@login_required
def blog (request):
    posts = Post.objects.all()
    return render(request, "Indice/Plantillas/blog.html",{'posts': posts, 'user_avatar':buscar_url_avatar(request.user)}) 
