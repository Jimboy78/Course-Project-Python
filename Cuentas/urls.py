from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name='login'),
    path('logout/', LogoutView.as_view(template_name="Indice/Plantillas/index.html"), name='logout'),
    path('editar/', views.Editar, name='editar'),
]
 