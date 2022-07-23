from django.urls import path
from . import views
from .views import inicio


urlpatterns = [
    path('posteos/', views.ListadoPosteos.as_view(), name='listado_posteos'),
    path('crear-posteo/', views.CrearPosteo.as_view(), name='crear_posteo'),
    path('editar-posteo/<int:pk>/', views.EditarPosteo.as_view(), name='editar_posteo'),
    path('eliminar-posteo/<int:pk>/', views.EliminarPosteo.as_view(), name='eliminar_posteo'),
    path('mostrar-posteo/<int:pk>/', views.MostrarPosteo.as_view(), name='mostrar_posteo'),
]
