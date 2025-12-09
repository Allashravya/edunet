"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from freelance.views import dashboard, home,login_view,register,freelance
from freelance.views import profile,courses,skills,logout,application_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('freelance/', freelance, name='freelance'),
    path('home/',home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/',profile, name='profile'),
    path('courses/',courses, name='courses'),
    path('skills/',skills, name='skills'),
    path('logout/',logout, name='logout'),
    path('application/',application_view, name='application'),
]