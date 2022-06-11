from django.urls import path
from doctor.views import*



urlpatterns=[

    path('reg/',dr_regform,name="dr_regfrom"),
    path('login/',dr_login,name="dr_log"),
    path('regact/',dr_regaction,name="regAct"),
    path('drhome/',dr_loadhomepage,name="loadhomepage"),
    path('logact/',dr_logaction,name="logAct"),
    path('dr_profile/',loadprofile,name="dr_pro"),
    path('apmnts/',loadappointments,name="appointmentslist"),
]
