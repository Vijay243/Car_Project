from django.shortcuts import render,redirect
from Admin_app.models import Manager_Model
from Manager_app.models import Driver_Model,Car_Model
from Manager_app.forms import Driver_Form,Car_Form
from django.contrib import messages
from django.views.generic import View
def manager_loginCheck(request):
    un = request.POST["username"]
    pas = request.POST["password"]
    try:
        res = Manager_Model.objects.get(Email=un,password=pas)
        request.session["s_id"]=res.idno  
        return render(request,"Manager_success_home.html")
    except Manager_Model.DoesNotExist:
        messages.success(request,"Enter Valid Credential")
        return redirect('manager_login')
    
def managers_profile(request): 
    res = request.session.get("s_id", None)
    if res:
        data = Manager_Model.objects.filter(idno=res)
        return render(request,"manager_profile.html",{"data":data})
    else:
        return redirect('manager_login')

def manager_logout(request):
    del request.session["s_id"]
    return redirect('manager_login')

def manager_login(request):
    res = request.session.get("s_id", None)
    if res:
        return render(request,"Manager_success_home.html")
    else:
        return render(request,"manager.login.html")

def add_cars(request):
    res = request.session.get("s_id", None)
    if res:
        return render(request,"add_cars.html",{"form":Car_Form()})
    else:
        return render(request,"manager.login.html")

class Car_Save(View):
    def post(self, request):
        res = request.session.get("s_id", None)
        if res:
            cf = Car_Form(request.POST, request.FILES)
            if cf.is_valid():
                cf.save()
                return render(request, "add_cars.html", {"msg": "Details Saved"})
            else:
                return render(request, "add_cars.html", {"form": cf})
        else:
            return redirect('manager_login')

def add_driver(request):
    res = request.session.get("s_id", None)
    if res:
        return render(request, "add_driver.html", {"form": Driver_Form()})
    else:
        return render(request, "manager.login.html")

class Driver_Save(View):
    def post(self, request):
        res = request.session.get("s_id", None)
        if res:
            id =  request.POST["d_id"]
            name = request.POST["d_name"]
            lic = request.POST["d_licence"]
            car = request.POST.getlist("d_car")
            age = request.POST["d_age"]
            gender = request.POST["d_gender"]
            exp = request.POST["d_expireance"]
            mob = request.POST["d_mobile"]
            email = request.POST["d_email"]
            address =  request.POST["d_address"]
            img = request.FILES["d_image"]
            dm = Driver_Model(d_id=id,d_name=name,d_licence=lic,d_age=age,d_gender=gender,d_expireance=exp,d_mobile=mob,d_email=email,d_address=address,d_image=img)
            dm.save()
            dm.d_car.set(car)
            return render(request, "add_driver.html", {"msg": "Details Saved"})
        else:
            return redirect('manager_login')


