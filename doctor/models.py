from django.db import models

# Create your models here.
class Login(models.Model):
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class dr_reg(models.Model):
    name=models.CharField(max_length=30)
    specialist=models.CharField(max_length=30)
    hospital=models.CharField(max_length=30)
    consultation_period=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    fee=models.IntegerField(default=0)
    login=models.ForeignKey(Login,models.CASCADE)
    status=models.IntegerField(default=0)
