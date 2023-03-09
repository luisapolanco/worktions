from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import User,  Service, Category


class SignUpUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)
    class Meta: 
        model = User

        fields = [
            'id',
            'name',
            'date_of_birth',
            'address',
            'email',
            'city',
            'phone',
            'gender',
            'username',
            'password'
        ]
        labels = {
            'id' : 'Cédula',
            'name' : 'Nombre',
            'date_of_birth' : 'Fecha de nacimiento',
            'address' : 'Dirección',
            'email' : 'Correo electrónico',
            'city' : 'Ciudad',
            'phone' : 'Teléfono',
            'gender': 'Género',
            'username' : 'Nombre de usuario',
            'password' : 'Contraseña',
        }
        widgets = {
            'id': forms.TextInput(),
            'name' : forms.TextInput(),
            'date_of_birth' : forms.DateInput( ),
            'address': forms.TextInput(),
            'email' : forms.TextInput(),
            'city': forms.TextInput(),
            'phone': forms.TextInput(),
            'gender' : forms.SelectMultiple(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')]),
            'username': forms.TextInput(),
        }

#formulario servicios 
class Post_Service(forms.ModelForm):
    
    category_id = forms.ModelChoiceField(queryset=Category.objects.all())
    user_id =  forms.ModelChoiceField(queryset=User.objects.all())
        
    class Meta:
        model = Service
        fields = [
            'category_id',
            'user_id',
            'title',
            'description',
            'images'
        ]
        labels={
            'category_id':'Elegir categoria ajustada a su servicio',
            'user_id':'Cedula',
            'Title':'Titulo del servicio',
            'description':'Ingrese descripcion de su servicio a prestar',
            'images':'Muestra tus trabajos anteriores'
        }
        widgets={
            'description': forms.Textarea(attrs={"rows":5, "cols":50}),
            'title': forms.TextInput(),
        }
