from django import forms
from Modules.Services.models import Customer, Contractor

class SignUpCustomerForm(forms.ModelForm):
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
        }
        widgets = {
            'id': forms.TextInput(),
            'name' : forms.TextInput(),
            'date_of_birth' : forms.DateInput( ),
            'address': forms.TextInput(),
            'email' : forms.TextInput(),
            'city': forms.TextInput(),
            'phone': forms.TextInput(),
            'gender' : forms.SelectMultiple( choices=['Femenino','Masculino'] ),
        }