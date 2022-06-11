from django.shortcuts import render,redirect
from patient.models import *
from doctor.models import *
# Create your views here.
def p_regform(request):
    return render(request,"p_registration.html")


def p_login(request):
    return render(request,"p_login.html")


def p_regformaction(request):
    if request.method=="POST":
        msg=""
        p_name=request.POST["name"]
        p_personaladdress=request.POST["address"]
        p_gender=request.POST["sex"]
        p_place=request.POST["place"]
        p_pincode=request.POST["pincode"]
        p_emailid=request.POST["email"]
        p_dob= request.POST["DOB"]
        p_mob= request.POST["MOB"]
        p_username=request.POST["username"]
        p_password=request.POST["psw"]
        login=p_Login(user_name=p_username,password=p_password)
        login.save()
        z=p_reg(name=p_name,personal_address=p_personaladdress,gender=p_gender,place=p_place,pincode=p_pincode,email_id=p_emailid,dob=p_dob,mob=p_mob,login=login)
        z.save()
        if z:
            msg="success"
        else:
            msg="failed"
        return render(request,"p_registration.html",{"z":msg})



def p_loginaction(request):
    msg = ''
    if request.POST["user_id"] and request.POST["pswd"]:
        user_id = request.POST["user_id"]
        password = request.POST["pswd"]
        if user_id =="user" and password =="user":
            return render(request,"p_home.html")
        else:
            try:
                reg = p_Login.objects.get(user_name=user_id,password=password)
                print("regobj=", reg)
                if reg:
                    mobj = p_reg.objects.get(login=reg)
                    request.session["userid"] = mobj.id
                    return render(request,"p_home.html",{"mreg":mobj})
                else:
                    print("y=",user_id,"pass",password)
            except:
                msg="invalid"
                print("y=",user_id, "pass",password)
                return render(request,"p_login.html",{"msg":msg})



def loaddoctordetails(request):
    if request.method=="POST":
        z=request.POST["specialisation"]
        doctorlist=dr_reg.objects.filter(specialist=z)
        return render(request, "doctors_details.html", {"doctor_list": doctorlist})

    else:
        dr_j=dr_reg.objects.all()
        return render(request,"doctors_details.html",{"dr_j":dr_j})
def Makeappointment(request):
    w = request.POST["date"]
    b = request.POST["doctor_id"]
    doctor = dr_reg.objects.get(id=b)
    mobj = p_reg.objects.get(id=request.session["userid"])
    t=Appointment()
    t.patient=mobj
    t.dr_doctor=doctor
    t.date=w
    t.save()
    return redirect("dr_det")









