"""Car_Newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
from Manager_app import views

urlpatterns = [
    path('manager_login/',views.manager_login,name="manager_login"),
    path('manager_loginCheck/',views.manager_loginCheck,name="manager_loginCheck"),
    path('managers_profile/',views.managers_profile,name="managers_profile"),
    path('manager_logout/',views.manager_logout,name="manager_logout"),
    path('add_cars/',views.add_cars,name="add_cars"),
    path('car_save/',views.Car_Save.as_view(),name="car_save"),
    path('add_driver/',views.add_driver,name="add_driver"),
    path('driver_save/',views.Driver_Save.as_view(),name="driver_save")
]
