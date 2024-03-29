"""worktions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Modules.Services import views as servicesViews
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'worktions'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', servicesViews.home, name="home"),
    path('register/', servicesViews.signUp, name="register"),
    path('post-service', servicesViews.postService,name="post-service"),
    path('profile',servicesViews.profile, name="profile" ),
    path('accounts/',include('django.contrib.auth.urls'), name="accounts/login"),
    path('edit_profile/', servicesViews.edit_profile,name="edit_profile"),
    path('delete_service/<id>', servicesViews.delete_service,name="delete_service"),
    path('edit_service/<id>', servicesViews.edit_service_template,name="edit_service_template"),
    path('edit_service', servicesViews.edit_service, name="edit_service"),
    path('analitica/', servicesViews.analiticaGrafica,name="analitica"),
    path('service/<int:pk>/', servicesViews.service_detail_view, name='service_detail'),
    path('user/profile/<str:pk>/', servicesViews.userDetail.user_detail_view, name='user-detail'),
    path('save_review/<int:sid>/', servicesViews.save_review, name='save_review'),
    path('', include('chat.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
