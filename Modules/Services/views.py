from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import Http404, HttpRequest, HttpResponse
from .models import *
from django.contrib.auth.views import LoginView
from .forms import  Post_Service, CustomUserCreationForm
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
    return render(request, 'profile.html', {'services': services, 'user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def edit_service_template(request, id):
    service = Service.objects.get(id=id)    
    return render(request, 'edit_service.html', {'service': service})

def edit_service(request):
    print(request.POST['category'])
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
    data = {
        'form': Post_Service()
    }
    if request.method == 'POST':
        form2 = Post_Service(request.POST, request.FILES)
        print(request.POST)
        print(form2)
        if form2.is_valid():
            ServiceTemp = Service()
            ServiceTemp.category = form2.cleaned_data['category']
            ServiceTemp.user = request.user
            ServiceTemp.title = form2.cleaned_data['title']
            ServiceTemp.description = form2.cleaned_data['description']
            ServiceTemp.images = form2.cleaned_data['images']
            ServiceTemp.save()
            data['mensaje'] = 'Servicio agregado correctamente'
            return redirect(to='/home')   
    return render(request, 'service.html', data)


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


    dictS = {
        **dictC,
        **dictG,
        **dictCi,
            }   

    return render(request, 'analitica.html', context=dictS)


class serviceDetail(generic.DetailView):
    model = Service
    template_name = 'service_detail.html'

    def service_detail_view(request, pk):
        try:
            service_id = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404("Este servicio no existe")

        return render(
            request,
            'service_detail.html',
            context={'service': service_id, }
        )


class userDetail(generic.DetailView):
    model = User
    template_name = 'user_detail.html'

    def user_detail_view(request, pk):
        try:
            user = User.objects.get(pk=pk)
            services = Service.objects.filter(user_id=user.id)
        except User.DoesNotExist:
            raise Http404("Este usuario no existe")

        return render(
            request,
            'user_detail.html',
            context={'user_info': user, 'services': services}
        )