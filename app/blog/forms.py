from django import forms
from .models import Post


class FormularioPost(forms.ModelForm): #Herada de models forms
    class Meta:
        model=Post
        fields = ('categoria','titulo','contenido','imagen')   #Campos a mostrar en el formulario

