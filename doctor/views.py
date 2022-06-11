from django.shortcuts import render,redirect
from doctor.models import *
from patient.models import *


# Create your views here.


def dr_regform(request):
    return render(request,"dr_reg.html")


def dr_login(request):
    return render(request,"dr_login.html")


def dr_loadhomepage(request):
    return render(request,"dr_home.html")


def dr_regaction(request):
    if request.method=="POST":
        msg=""
        dr_name=request.POST["name"]
        dr_specilist=request.POST["specialist"]
        dr_hospital=request.POST["n_hospt"]
        dr_consultationperiod=request.POST["time"]
        dr_address=request.POST["address"]
        dr_fee=request.POST["fee"]
        dr_username=request.POST["username"]
        dr_password=request.POST["psw"]
        login=Login(user_name=dr_username,password=dr_password)
        login.save()
        x=dr_reg(name=dr_name,specialist=dr_specilist,hospital=dr_hospital,consultation_period=dr_consultationperiod,address=dr_address,fee=dr_fee,login=login)
        x.save()
        if x:
            msg="success"
        else:
            msg="failed"

        return render(request,"dr_reg.html",{"x":msg})



def dr_logaction(request):
    msg=''
    if request.POST["user_id"] and request.POST["pswd"]:
        user_id=request.POST["user_id"]
        password=request.POST["pswd"]
        if user_id=="admin" and password=="admin":
            return render(request,"dr_home.html")
        else:
            try:
                reg=Login.objects.get(user_name=user_id,password=password)
                print("regobj=",reg)
                if reg:
                    mobj=dr_reg.objects.get(login=reg)
                    request.session["userid"]=mobj.id
                    return render(request,"dr_home.html",{"mreg":mobj})
                else:
                    print("y=",user_id,"pass",password)
            except:
                msg="invalid"
                print("y=",user_id,"pass",password)
                return render(request,"dr_login.html",{"msg":msg})




def loadprofile(request):
    drid=request.session["userid"]
    dr_details=dr_reg.objects.get(id=drid)
    return render(request,"dr_profile.html",{"details":dr_details})


def loadappointments(request):
    # apmnt_list=Appointment.objects.all()
    # p_list=p_reg.objects.all().exclude(id__in=apmnt_list.values('patient'))
    #p_list=p_reg.objects.all().exclude(id__in=apmnt_list.values('patient'))
    # print(p_list)
    # return render(request,"appointments.html",{"preg":p_list,"apmnt":apmnt_list})

    # drid=request.session["userid"]
    # apmnt_list=Appointment.objects.get(id=drid)
    drid = request.session["userid"]
    dr_details = dr_reg.objects.get(id=drid)
    apmnt_list = Appointment.objects.filter(dr_doctor=dr_details)
    return render(request,"appointments.html",{"apmnts":apmnt_list})






