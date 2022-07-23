from django import forms

class BusquedaPosteo(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)