from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import Http404, HttpRequest, HttpResponse
from .models import *
from django.contrib.auth.views import LoginView
from .forms import Post_Service, CustomUserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
import pandas as pd
from .utils import get_plot 
import matplotlib.pyplot as plt
from django.db.models import Count
from django.views import generic


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

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


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
            service.category = form2.cleaned_data['category']
            service.user_id = form2.cleaned_data['user_id']
            service.description = form2.cleaned_data['description']
            service.images = form2.cleaned_data.get('id_images')
            #file_access = default_storage.save('media/servicios/', ContentFile(service.images.read()))
            service.title = form2.cleaned_data['title']
            service.save()
            data['mensaje'] = 'Servicio agregado correctamente'
            redirect('/home')
    return render(request, 'service.html', data)

def analiticaTabla(request): 
    #TABLAS
    item=Service.objects.values("category").annotate(count=Count('category'))
    df = pd.DataFrame(item)
    dictS={
        "df":df.to_html(),
    }
    print(dictS)

    return render(request,'analitica.html',context=dictS)
    '''
    #GRAFICO
    items=Service.objects.all()
    x=[x.category for x in items]
    y=[y.user_id_id for y in items]
    chart = get_plot(x,y,"category","ids","categorias")
    return render(request,'analitica.html',{'chart':chart})'''


class serviceDetail( generic.DetailView ):
    model = Service
    template_name = 'service_detail.html'

    def service_detail_view(request, pk):
        try:
            service_id=Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404("Este servicio no existe")

        return render(
            request,
            'service_detail.html',
            context={'service':service_id,}
        )


    


