"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from mydjango.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('myapp/',include('myapp.urls')),
    path('about/',about),
    path('contact/',contact),
    path('services/',services),
    # path('dynamic/<str:name>/',dynamic)
    path('dynamic/<str:name>/',dynamic),
    # add/45/55/  => sum of 45 and 55 is 100
    path('add/<int:num1>/<int:num2>/',add),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
