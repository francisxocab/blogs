from django.contrib import admin
from .models import Disco, Cancion, Artista, CancionDisco, Comentario


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'titulo', 'debut', 'cancion_disco',
                    'destacado', 'visible', 'imagen')
    search_fields = ('titulo', 'user__username', 'user__email')
    list_filter = ('creado', 'modificado')
    list_editable = ('cancion_disco', 'destacado', 'visible',)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url',)
        form = super(ArtistaAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['perfil'].initial = request.user.perfil
        return form


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Disco)
class DiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(CancionDisco)
class CancionDiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cancion', 'disco')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'artista', 'comentario', 'visible')