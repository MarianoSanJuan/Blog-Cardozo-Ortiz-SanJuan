from django.urls import path
from .views import login, registro, perfil, editar_perfil, ChangePasswordView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', ChangePasswordView.as_view(), name='cambiar_password'),
]
