from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from .models import User,  Service
from .choices import BARRIOS_MED


class CustomUserCreationForm(UserCreationForm):
    barrio = forms.ChoiceField(choices=BARRIOS_MED)
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
            'barrio', 
            'phone', 
            'gender'
        ]
        labels={
            'username':'Nombre de usuario:', 
            'email':'Correo electrónico', 
            'name':'Nombres', 
            'id':'Cedula', 
            'date_of_birth':'Fecha de nacimiento', 
            'address':'Dirección', 
            'city':'Ciudad',
            'barrio':'Barrio', 
            'phone' : 'Telefono',
            'gender': 'Género'
        }
        widgets={
            'date_of_birth': forms.DateInput()
        }
#formulario servicios 
class Post_Service(forms.ModelForm):
    category_choices = (
        ("Limpieza", "Limpieza"),
        ("Manufactura", "Manufactura"),
        ("Automotriz", "Automotriz"),
        ("Cuidado_de_hogar", "Cuidado_de_hogar"),
        ("Cuidado_de_mascotas", "Cuidado_de_mascotas")
    )
    category = forms.ChoiceField(choices=category_choices)
    #user_id =  forms.CharField(max_length=100, required=False)
    class Meta:
        model = Service
        fields = [
            'category',
            'title',
            'description',
            'images'
        ]
        labels={
            'category':'Elegir categoria ajustada a su servicio',
            'Title':'Titulo del servicio',
            'description':'Ingrese descripcion de su servicio a prestar',
            'images':'Muestra tus trabajos anteriores'
        }
        widgets={
            'description': forms.Textarea(attrs={"rows":5, "cols":50}),
            'title': forms.TextInput(),
        }

        
class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=254)
    name = forms.CharField(max_length=200, required=False)
    #id
    address = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=20, required=False)
    phone= forms.CharField(max_length=15, required=False)
    gender = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = User
        fields = ['username','email','name', 'address', 'city','phone','gender']

