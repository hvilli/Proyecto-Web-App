from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=100, required = True)
    email = forms.EmailField(label = "Correo", required = True)
    contenido = forms.CharField(label = "Contendo", required = False, widget = forms.Textarea)