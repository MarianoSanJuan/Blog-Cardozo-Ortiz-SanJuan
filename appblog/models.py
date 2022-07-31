from django.db import models

# Create your models here.

#Clase basada en vista: Blog

class Posteos(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    autor = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return (f'This post belongs to {self.autor}')
    
    