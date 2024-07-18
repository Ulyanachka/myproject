"""
URL configuration for myproject project.

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
from django.urls import path, include
from myapp3.views import index
from myapp4.views import add_user
from myappform.views import upload_product_photo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('myapp.urls')),
    path('les3/', include('myapp3.urls')),
    path('', index, name='index'),
    path('les4/', include('myapp4.urls')),
    path('user/', add_user, name='add_user'),
    path('image/', upload_product_photo, name='upload_product_photo'),
    # path('__debug__/', include("debug_toolbar.urls")),
    path('les6/', include('myapp6.urls')),
]
