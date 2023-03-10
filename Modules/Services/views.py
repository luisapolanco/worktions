from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpRequest
import pdb
from .models import *
from django.contrib.auth.views import LoginView
from .forms import Post_Service, CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    searchTerm = request.GET.get('searchService')
    if searchTerm:
        services = Service.objects.filter(title__icontains=searchTerm)
    else:
        services = Service.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'services': services, 'num_visits': num_visits})

def profile(request):
    return render(request, 'profile.html')

def info_usuario(request):
    return render(request, 'info_usuario.html')


'''def signUpUser(request):
    data = {
        'form': SignUpUserForm()
    }

    if request.method == 'POST':
        form2 = SignUpUserForm(request.POST)
        if form2.is_valid():
            #form2.save()
            user = User()
            user.id = form2.cleaned_data['id']
            user.name = form2.cleaned_data['name']
            user.date_of_birth = form2.cleaned_data['date_of_birth']
            user.address = form2.cleaned_data['address']
            user.email = form2.cleaned_data['email']
            user.city = form2.cleaned_data['city']
            user.phone = form2.cleaned_data['phone']
            user.gender = form2.cleaned_data['gender']
            user.username = form2.cleaned_data['user_name']
            user.password = form2.cleaned_data['password']

            user.save()

            data['mensaje'] = 'Usuario creado correctamente'
            redirect('/home')

    return render(request, 'signup.html', data)'''

def signUp(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="/home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def postService(request):
    data={
        'form': Post_Service() 
    }

    if request.method == 'POST':
        form2 = Post_Service(request.POST,request.FILES)
        print(form2)
        if form2.is_valid():
            #form2.save()
            service = Service()
            service.category_id = form2.cleaned_data['category_id']
            service.user_id = form2.cleaned_data['user_id']
            service.description = form2.cleaned_data['description']
            service.images = form2.cleaned_data.get('id_images')
            #file_access = default_storage.save('media/servicios/', ContentFile(service.images.read()))
            service.title = form2.cleaned_data['title']
            service.save()
            data['mensaje'] = 'Servicio agregado correctamente'
            redirect('/home')
    return render(request, 'service.html', data)


