from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from apps.users.models import Perfil

class Disco(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('nombre',)
 
    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
        return self.nombre

class Artista(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255, unique=True)
    url = models.SlugField(max_length=255, unique=True)
    resumen = RichTextField()
    contenido = RichTextField()
    vistas = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50)
    debut = models.PositiveIntegerField()
    ciudad_de_origen = models.CharField(max_length=50)
    imagen = models.ImageField (upload_to='artista/images/')
    
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('creado',)
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Artista, self).save(*args, **kwargs)  
    
    
    def __str__(self):
        return f'{self.debut} - {self.user.username}'


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=5000)
    visible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True) 

class Contacto(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


# Create your models here.
