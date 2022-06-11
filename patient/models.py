from django.db import models
from doctor.models import *


# Create your models here.
class p_Login(models.Model):
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class p_reg(models.Model):
    name=models.CharField(max_length=30)
    personal_address=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    pincode=models.IntegerField(default=0)
    email_id=models.CharField(max_length=30)
    dob= models.DateField()
    mob= models.IntegerField(default=0)
    login=models.ForeignKey(p_Login,models.CASCADE)
    status=models.IntegerField(default=0)
class Appointment(models.Model):
    patient=models.ForeignKey(p_reg,on_delete=models.CASCADE)
    dr_doctor=models.ForeignKey(dr_reg,on_delete=models.CASCADE)
    date=models.DateTimeField()