"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# Since we are adding a function in the views we need to import the views file
# to continue to use it.

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciaz/', views.firstcar),
    path('', views.landing, name='landing'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
