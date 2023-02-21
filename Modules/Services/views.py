from django.shortcuts import render, redirect
from django.http import HttpRequest

from .forms import SignUpCustomerForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signUpCustomer(request):
    data = {
        'form' : SignUpCustomerForm()
    }

    if request.method == 'POST':
        form2 = SignUpCustomerForm(request.POST)
        if form2.is_valid():
            form2.save()
            data['mensaje'] = 'Usuario creado correctamente'

    return render(request, 'signup.html', data)
