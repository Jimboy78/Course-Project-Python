from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Inicio, name="index"),
    path('logout/', LogoutView.as_view(template_name="Indice/Plantillas/index.html"), name='logout'),
    path('about_us/', views.AboutUs, name="about_us"),
    path('blog/',views.Blog, name="blog"),
    path('logout/', LogoutView.as_view(template_name="index.html"), name='logout'),
]
 