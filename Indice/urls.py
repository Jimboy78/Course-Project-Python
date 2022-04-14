from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    
    path('', views.Inicio, name="index"),
    path('about_us/', views.AboutUs, name="about_us"),
    path('blog/', views.Blog, name="blog"),
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name='login'),
    path('logout/', LoginView.as_view(template_name="index.html"), name='logout'),
    
]
 