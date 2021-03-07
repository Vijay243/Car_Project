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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Admin_app import views
from Car_Newproject import settings

urlpatterns = [
    path('admin_Home/',TemplateView.as_view(template_name="admin_home.html"),name="admin_home"),
    path('admin_check/', views.admin_check, name="admin_check"),
    path('manager/', views.Manager_save.as_view(), name="manager"),
    path('managers_all/', views.Manager_details.as_view(), name="managers_all"),
    path('admin_success/', views.admin_success, name="admin_success"),
    path('add_manager/',views.add_manager,name="add_manager"),
    path('cars_view/',views.cars_view,name="cars_view"),
    path('drivers_view/',views.drivers_view,name="drivers_view"),
    path('customer_view/',views.customer_view,name="customer_view"),
    path('send_mail_manager/',views.send_mail_manager,name="send_mail_manager"),
    path('update_manager/<int:pk>',views.Update_Mnager.as_view(),name="update_manager"),
    path('delete_manager/<int:pk>',views.Delete_Manager.as_view(),name="delete_manager"),
    #path('delete_succes/,views.Delete_Success.as_view(),name ="delete_succes")
   # path('admin_logut/',views.admin_logut,name="admin_logut"),
]
if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)