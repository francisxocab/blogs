from django.contrib import admin
from .models import Disco #importamos desde models.py nuestra class

admin.site.register(Disco) #registra desde nuestra class, el object que queremos mostrar en el admin de django

# Register your models here.
