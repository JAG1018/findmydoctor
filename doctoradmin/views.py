from django.shortcuts import render

def loadmainhome(request):
    return render(request,"index.html")
def loadloginpage(request):
    return render(request,"")
# Create your views here.
