from django import forms

class FormMessage(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form_ms",
        "placeholder": "Escribe tu mensaje",
    }))