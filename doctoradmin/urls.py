from django.urls import path
from doctoradmin.views import *
from doctor.views import *
from patient.views import *
urlpatterns=[
    path('mainhome/',loadmainhome,name="mainhome"),
    path('login/',dr_login,name="dr_login"),
    path('reg/',dr_regform,name="dr_regfrm"),
    path('preg/',p_regform,name="p_regfrm"),
    # path('plogin/', p_login, name="p_log"),


]