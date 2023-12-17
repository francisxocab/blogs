from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comentario, Artista, CancionDisco


class CrearComentarioForm(forms.ModelForm):

    comentario = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comentario
        fields = ('user', 'perfil', 'artista', 'comentario')


class AutoForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['titulo', 'resumen', 'contenido', 'destacado', 'cancion_disco',
                  'visible', 'imagen']

    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    resumen = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control'})
    )
    contenido = forms.CharField(
        widget=CKEditorWidget(
            attrs={'class': 'form-control'})
    )
    destacado = forms.BooleanField(
        widget=forms.CheckboxInput(),
    )
    cancion_disco = forms.ModelChoiceField(
        queryset=CancionDisco.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    visible = forms.BooleanField(
        widget=forms.CheckboxInput()
    )