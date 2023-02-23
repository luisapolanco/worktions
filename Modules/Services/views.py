from django.shortcuts import render, redirect
from django.http import HttpRequest
import pdb
from .forms import SignUpCustomerForm, SignUpContractorForm
from .models import Service

# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchService')
    if searchTerm:
        services = Service.objects.filter(id__icontains=searchTerm)
    else:
        services = Service.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'services': services})


def signUpCustomer(request):
    data = {
        'form': SignUpCustomerForm()
    }

    if request.method == 'POST':
        form2 = SignUpCustomerForm(request.POST)
        breakpoint()
        if form2.is_valid():
            form2.save()
            data['mensaje'] = 'Usuario creado correctamente'
            redirect('home')

    return render(request, 'signup.html', data)


def signUpContractor(request):
    data = {
        'form': SignUpContractorForm()
    }

    if request.method == 'POST':
        form2 = SignUpContractorForm(request.POST)
        print(form2)
        if form2.is_valid():
            form2.save()
            data['mensaje'] = 'Usuario creado correctamente'
            redirect('home')

    return render(request, 'signup.html', data)
