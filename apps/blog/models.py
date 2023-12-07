from django.db import models

class Disco(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    duracion = models.IntegerField()
    generos = models.IntegerField()
    formato = models.CharField(max_length=50)
    precio = models.IntegerField() 
    image = models.ImageField(upload_to= 'disco_images/')
    def __str__(self):
        return f'{self.nombre}, {self.fecha_lanzamiento}, {self.duracion}, {self.generos}, {self.formato}, {self.precio}'

class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    duracion = models.IntegerField()
    genero = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}, {self.fecha_lanzamiento}, {self.duracion}, {self.genero}'


class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    debut = models.IntegerField()
    ciudad_de_origen = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}, {self.debut}, {self.ciudad_de_origen}' 

class Compositor(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}'

class Produccion(models.Model):
    estudio_de_grabacion = models.CharField(max_length=50)
    


# Create your models here.
