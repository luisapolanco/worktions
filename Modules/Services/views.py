from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpRequest
import pdb
from .models import *

from .forms import SignUpCustomerForm, SignUpContractorForm, Post_Service

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
        if form2.is_valid():
            #form2.save()
            customer = Customer()
            customer.id = form2.cleaned_data['id']
            customer.name = form2.cleaned_data['name']
            customer.date_of_birth = form2.cleaned_data['date_of_birth']
            customer.address = form2.cleaned_data['address']
            customer.email = form2.cleaned_data['email']
            customer.city = form2.cleaned_data['city']
            customer.phone = form2.cleaned_data['phone']
            customer.gender = form2.cleaned_data['gender']
            customer.user_name = form2.cleaned_data['user_name']
            customer.password = form2.cleaned_data['password']

            customer.save()

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
            #form2.save()

            contractor = Contractor()
            contractor.id = form2.cleaned_data['id']
            contractor.name = form2.cleaned_data['name']
            contractor.date_of_birth = form2.cleaned_data['date_of_birth']
            contractor.address = form2.cleaned_data['address']
            contractor.email = form2.cleaned_data['email']
            contractor.city = form2.cleaned_data['city']
            contractor.phone = form2.cleaned_data['phone']
            contractor.gender = form2.cleaned_data['gender']
            contractor.user_name = form2.cleaned_data['user_name']
            contractor.password = form2.cleaned_data['password']

            contractor.save()

            data['mensaje'] = 'Usuario creado correctamente'
            redirect('home')

    return render(request, 'signup.html', data)

def postService(request):
    data={
        'form': Post_Service() 
    }

    if request.method == 'POST':
        form2 = Post_Service(request.POST)
        print(form2)
        if form2.is_valid():
            #form2.save()
            service = Service()
            service.category_id = form2.cleaned_data['category_id']
            service.contractor_id = form2.cleaned_data['contractor_id']
            service.description = form2.cleaned_data['description']
            #service.images = form2.cleaned_data.get('id_images')
            #file_access = default_storage.save('media/servicios/', ContentFile(service.images.read()))
            service.title = form2.cleaned_data['title']

            service.save()

            data['mensaje'] = 'Servicio agregado correctamente'
            redirect('home')
    return render(request, 'service.html', data)