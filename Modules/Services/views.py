from django.shortcuts import render, redirect
from django.http import HttpRequest

from Modules.Services.forms import SignUpCustomerForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signUpCustomer(request: HttpRequest):
    # if request.POST == 'POST':
    form = SignUpCustomerForm(request.POST)
    
    if form.is_valid():
        form.save()

    return render(request, 'signup.html', {'form': form})
    # return redirect('/login')
    # else:
        # form = signUpCustomer(request.POST)
    
    # return render(request, 'services/signup.html', {'form': form})
