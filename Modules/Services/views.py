from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.views import LoginView
from .forms import  Post_Service, CustomUserCreationForm, ReviewAdd
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
import pandas as pd
from .utils import get_plot
import matplotlib.pyplot as plt
from django.db.models import Count, Avg, Q,Subquery, OuterRef,Sum
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import messages
from collections import OrderedDict
User = get_user_model()


# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchService')
    if searchTerm:
        services = Service.objects.filter(title__icontains=searchTerm)
    else:
        services = Service.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'services': services})


def profile(request):
    services = Service.objects.filter(user_id=request.user.id)
    data = CustomUserCreationForm()
    serviceForm = Post_Service()
    
    return render(request, 'profile.html', {'services': services, 'user': request.user, 'form': data, 'serviceForm': serviceForm})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        id = request.POST['id']
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        city = request.POST['city']
        barrio = request.POST['barrio']
        phone = request.POST['phone']
        gender = request.POST['gender']

        user = User.objects.get(id=id)    
        user.username = username
        user.email = email
        user.name = name
        user.date_of_birth = date_of_birth
        user.address = address
        user.city = city
        user.barrio = barrio
        user.phone = phone
        user.gender = gender
        user.save()
        return redirect(to="/profile")
    

@login_required
def edit_service_template(request, id):
    service = Service.objects.get(id=id)    
    return render(request, 'edit_service.html', {'service': service})

def edit_service(request):
    id = request.POST['id']
    category = request.POST['category']
    title = request.POST['title']
    description = request.POST['description']
    images = request.FILES['images']

    service = Service.objects.get(id=id)    
    service.category = category
    service.title = title
    service.description = description
    service.images = images
    service.save()
    return redirect(to="/profile")

def signUp(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="/home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def delete_service(request, id):
    service = Service.objects.get(id= id)
    service.delete()    
    return redirect(to="/profile")


@login_required
def postService(request):    
    if request.method == 'POST':       
        ServiceTemp = Service()
        ServiceTemp.category = request.POST['category']
        ServiceTemp.user = request.user
        ServiceTemp.title = request.POST['title']
        ServiceTemp.description = request.POST['description']
        ServiceTemp.images = request.FILES['images']
        ServiceTemp.save()        
        return redirect(to="/profile")


def analiticaGrafica(request):
    # consultas
    categories = Service.objects.values(
        "category").annotate(count=Count('category'))
    df = pd.DataFrame(categories)
    df1 = df.category.tolist()
    df = df['count'].tolist()
    dictC = {
        "df": df,
        "df1": df1,
    }

    genders = User.objects.values("gender").annotate(count=Count('gender'))
    genderData = pd.DataFrame(genders)
    genderLabel = genderData.gender.tolist()
    genderData = genderData['count'].tolist()
    dictG = {
        "genderData": genderData,
        "genderLabel": genderLabel,
    }

    cities = User.objects.values("city").annotate(count=Count('city'))
    cityData = pd.DataFrame(cities)
    cityLabel = cityData.city.tolist()
    cityData = cityData['count'].tolist()
    dictCi = {
        "cityData": cityData,
        "cityLabel": cityLabel,
    }

    barrios = User.objects.values('barrio').annotate(count=Count('service__category')).order_by('barrio')

# Obtener todas las categorías disponibles
    categorias = Service.objects.values_list('category', flat=True).distinct()

# Crear un diccionario para almacenar los datos de cada barrio
    data_por_barrio = {}

# Inicializar los valores de cada categoría para cada barrio
    for barrio in barrios:
        barrio_label = barrio['barrio']
        data_por_barrio[barrio_label] = {categoria: 0 for categoria in categorias}

# Obtener el número de servicios por categoría para cada barrio
    for barrio in barrios:
        barrio_label = barrio['barrio']
        servicios_por_categoria = Service.objects.filter(user__barrio=barrio_label).values('category').annotate(count=Count('category'))
        for servicio in servicios_por_categoria:
            categoria = servicio['category']
            count = servicio['count']
            data_por_barrio[barrio_label][categoria] = count

    # Preparar los datos para la gráfica
    barrioLabel = list(data_por_barrio.keys())
    barrioData = []
    for barrio in barrioLabel:
        data = [data_por_barrio[barrio][categoria] for categoria in categorias]
        barrioData.append(data)
    categorias = list(categorias)
    print(barrioData)
    print(barrioLabel)
    print(categorias)

    dictB = {
        'barrioData': barrioData,
        'barrioLabel': barrioLabel,
        'categorias': categorias,
    }


    dictS = {
        **dictC,
        **dictG,
        **dictCi,
        **dictB,
            }   

    return render(request, 'analitica.html', context=dictS)



def service_detail_view(request, pk):
        try:
            print("que se acabe ya")
            Zervice_id = Service.objects.get(pk=pk)
            reviewForm = ReviewAdd()
            print("que se acabe ya")
            re_list = Reviews.objects.filter(service_id = pk)
            print(re_list)
        except Service.DoesNotExist:
            raise Http404("Este servicio no existe")
        return render(
            request,
            'service_detail.html',
            {'service': Zervice_id, 'form':reviewForm, 'reviews':re_list}
        )


class userDetail(generic.DetailView):
    model = User
    template_name = 'user_detail.html'

    def user_detail_view(request, pk):
        try:
            user = User.objects.get(pk=pk)
            services = Service.objects.filter(user=user.id)
        except User.DoesNotExist:
            raise Http404("Este usuario no existe")

        return render(
            request,
            'user_detail.html',
            context={'user_info': user, 'services': services}
        )

def save_review(request, sid):
    service = Service.objects.get(pk=sid)
    user = request.user
    review = Reviews.objects.create(
        user = user,
        service = service,
        comments = request.POST['comments'],
        calification = request.POST['calification'],
    )
    return redirect(to=f'/service/{sid}')