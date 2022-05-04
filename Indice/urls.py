from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="index"),
    path('logout/', LogoutView.as_view(template_name="Indice/Plantillas/index.html"), name='logout'),
    path('about_us/', views.about_us, name="about_us"),
    path('blog/',views.blog, name="blog"),
]
 