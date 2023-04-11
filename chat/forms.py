from django import forms

class FormMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form_ms",
        "placeholder": "Escribe tu mensaje"
    }))