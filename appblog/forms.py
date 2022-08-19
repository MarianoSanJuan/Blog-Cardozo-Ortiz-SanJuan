from django import forms
from ckeditor.fields import RichTextFormField

class BusquedaPosteo(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)