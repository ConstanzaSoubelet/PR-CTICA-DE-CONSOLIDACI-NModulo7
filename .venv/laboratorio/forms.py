from django import forms
from .models import Laboratorio


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']

    # Agregar placeholder a cada campo
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del Laboratorio'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese la Ciudad del laboratorio'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese el Pais del laboratorio'}))
