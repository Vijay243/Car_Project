from django.shortcuts import render,redirect
from django.views.generic import View,ListView,UpdateView,DeleteView,DetailView
from django.contrib import messages
from .models import Manager_Model
from .forms import Manager_Form
from django.core.mail import send_mail
from Car_Newproject.settings import EMAIL_HOST_USER
from Manager_app.models import Car_Model,Driver_Model

def admin_check(request):
    user = request.POST["username"]
    pwd = request.POST["password"]
    if user == "admin" and pwd == "admin":
        request.session["s_id"] = 1000
        return render(request, "admin_success.html", {"form": Manager_Form()})
    else:
        messages.success(request, "Enter valid Credentials")
        return redirect('admin_home')
class Manager_details(ListView):
    model = Manager_Model
    template_name = "manager_view.html"
class Manager_save(View):
    def post(self, request):
        res = request.session.get("s_id", None)
        if res:
            ef = Manager_Form(request.POST,request.FILES)
            if ef.is_valid():
                ef.save()
                return render(request,"add_manager.html",{"msg":"Details Saved"})
            else:
                return render(request, "add_manager.html", {"form": ef})
        else:
            return redirect('admin_home')
    def get(self, request):
        res = request.session.get("s_id", None)
        if res:
            return render(request, "admin_success.html")
        else:
            return redirect('admin_home')
def admin_success(request):
    return render(request, "admin_success.html",)

def add_manager(request):
    return render(request,"add_manager.html",{"form": Manager_Form()})

def cars_view(request):
    car = Car_Model.objects.all()
    return render(request,"cars_view.html",{"car":car})

def drivers_view(request):
    driver = Driver_Model.objects.all()
    return render(request,"drivers_view.html",{"driver":driver})

def customer_view(request):
    return render(request,"customer_view.html")

def send_mail_manager(request):
    email=request.POST["e"]
    password = request.POST["p"]
    subject ="Manager Credentials"
    message = "username: "+email+",password: "+password
    send_mail(subject,message,EMAIL_HOST_USER,[email])
    messages.success(request, "Email sent successfully")
    return redirect('managers_all')

class Update_Mnager(UpdateView,ListView):
    template_name = "manager_update.html"
    model = Manager_Model
    fields = "__all__"
    success_url = '/managers_all/'

class Delete_Manager(DetailView,DeleteView):
    template_name = "manager_delete.html"
    model = Manager_Model
    fields = "__all__"
    success_url = '/managers_all/'

def admin_logut(request):
    del request.session["s_id"]
    return redirect('admin_home')