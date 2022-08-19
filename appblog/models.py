
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

#Clase basada en vista: Blog

class Posteos(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    contenido = RichTextField(null=True)
    autor = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True)
    image = models.ImageField(upload_to='imagepost', null=True, blank=True)
    
    def __str__(self):
        return (f'This posts belongs to {self.autor}')
    
    