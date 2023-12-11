from django.db import models

class Disco(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    duracion = models.CharField(max_length=50)
    generos = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    precio = models.IntegerField() 
    imagen = models.ImageField(upload_to= 'disco_images/')
    def __str__(self):
        return f'{self.nombre} - {self.fecha_lanzamiento} - {self.duracion} - {self.generos} - {self.formato} - {self.precio}'

class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    duracion = models.IntegerField()
    genero = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.fecha_lanzamiento} - {self.duracion} - {self.genero}'

class CancionDisco(models.Model):
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.cancion} - {self.disco}'


class Artista(models.Model):
    cancion_disco = models.ForeignKey(CancionDisco, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50)
    debut = models.IntegerField()
    ciudad_de_origen = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} - {self.debut} - {self.ciudad_de_origen}' 

class Compositor(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}'

class Produccion(models.Model):
    estudio_de_grabacion = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.estudio_de_grabacion}'
    


# Create your models here.
