from django import forms
from django.forms import ModelForm
from .models import Customer, Contractor

class SignUpCustomerForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)
    class Meta: 
        model = Customer

        fields = [
            'id',
            'name',
            'date_of_birth',
            'address',
            'email',
            'city',
            'phone',
            'gender',
            'user_name',
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
            'user_name' : 'Nombre de usuario',
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
            'user_name': forms.TextInput(),
        }



class SignUpContractorForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)
    class Meta: 
        model = Contractor

        fields = [
            'id',
            'name',
            'date_of_birth',
            'address',
            'email',
            'city',
            'phone',
            'gender',
            'user_name',
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
            'user_name' : 'Nombre de usuario',
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
            'user_name': forms.TextInput(),
        }