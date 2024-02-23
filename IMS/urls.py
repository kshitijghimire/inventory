"""
URL configuration for IMS project.

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
from django.urls import path
from .views import index
from product import views
from Inventory import views
from Category import views
from customer import views
from sales import views



urlpatterns = [
    path('', index, name='Home'),
    path('product/', views.home, name='Product'),
    path('Inventory/', views.home, name='Inventory'),
    path('Category/', views.home, name='Category'),
    path('customer/', views.home, name='customer'),
    path('sales/',views.home,name='sales'),
    
    path('admin/', admin.site.urls),
]
