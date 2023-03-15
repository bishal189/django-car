
from django.shortcuts import render
from .models import Team

# Create your views here.


def home(request):
    teams=Team.objects.all()
    context={
        'teams':teams,
    }

    return render(request,'pages/home.html',context)

def about(request):
    teams=Team.objects.all()
    context={
        'teams':teams,
    }
    return render(request,'pages/about.html',context)
def service(request):
    return render(request,'pages/service.html')
def contact(request):
    return render(request,'pages/contact.html')
   
def car(request):
    return render(request,'pages/car.html')
def help(request):
    return render(request,'pages/help.html')

