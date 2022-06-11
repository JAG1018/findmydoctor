from django.urls import path
from patient.views import *

urlpatterns=[
    path('preg/',p_regform,name="p_regfrm"),
    path('plogin/',p_login,name="p_log"),
    path('regact/',p_regformaction,name="pregAct"),
    path('logact/',p_loginaction,name="p_logAct"),
    path('doctordetails/',loaddoctordetails,name="dr_det"),
    path('appointment/',Makeappointment,name="appointments")
]