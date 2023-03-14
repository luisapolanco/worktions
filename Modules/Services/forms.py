from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from .models import User,  Service


class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = User
        date_of_birth = forms.DateInput
        fields =[
            'username', 
            'email', 
            'name', 
            'id', 
            'date_of_birth', 
            'address', 
            'city', 
            'phone', 
            'gender'
            ]
#formulario servicios 
class Post_Service(forms.ModelForm):
    category_choices = (
        ("1", "Limpieza"),
        ("2", "Manufactura"),
        ("3", "Automotriz"),
        ("4", "Cuidado_de_hogar"),
         ("5", "Cuidado_de_mascotas")
    )
    category = forms.ChoiceField(choices=category_choices)
    user_id =  forms.ModelChoiceField(queryset=User.objects.all())
        
    class Meta:
        model = Service
        fields = [
            'category',
            'user_id',
            'title',
            'description',
            'images'
        ]
        labels={
            'category':'Elegir categoria ajustada a su servicio',
            'user_id':'Cedula',
            'Title':'Titulo del servicio',
            'description':'Ingrese descripcion de su servicio a prestar',
            'images':'Muestra tus trabajos anteriores'
        }
        widgets={
            'description': forms.Textarea(attrs={"rows":5, "cols":50}),
            'title': forms.TextInput(),
        }

