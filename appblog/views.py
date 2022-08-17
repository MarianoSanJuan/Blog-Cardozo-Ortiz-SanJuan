
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .forms import BusquedaPosteo
from .models import Posteos
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request,"index.html")

def about(request):
    return render(request, "about.html", {})

class CrearPosteo(LoginRequiredMixin,CreateView):
    model=Posteos
    template_name = 'posteos/crear_posteo.html'
    success_url = '/appblog/posteos'
    # prueba image
    fields = ['titulo', 'subtitulo', 'contenido',"autor","fecha_creacion","image"]
    

class ListadoPosteos(ListView):
    model=Posteos
    template_name = 'posteos/listado_posteos.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaPosteo()
        return context
    
class MostrarPosteo(DetailView):
    model = Posteos
    template_name = 'posteos/mostrar_posteo.html'
    
class EditarPosteo(LoginRequiredMixin,UpdateView):
    model=Posteos
    template_name = 'posteos/editar_posteo.html'
    success_url = '/appblog/posteos'
    # prueba image
    fields = ['titulo', 'subtitulo', 'contenido', 'autor',"image"]
    
class EliminarPosteo(LoginRequiredMixin,DeleteView):
    model=Posteos
    template_name = 'posteos/eliminar_posteo.html'
    success_url = '/appblog/posteos'