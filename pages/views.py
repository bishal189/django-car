
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'pages/home.html')
def about(request):
    return render(request,'pages/about.html')
def service(request):
    return render(request,'pages/service.html')
def contact(request):
    return render(request,'pages/contact.html')
   
def car(request):
    return render(request,'pages/car.html')
def help(request):
    return render(request,'pages/help.html')

