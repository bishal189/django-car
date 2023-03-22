
from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.


def home(request):
    teams=Team.objects.all()
    car_feature=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')
   
   
    
   
    
    context={
        'teams':teams,
        'car_feature':car_feature,
        'all_car':all_car
        
        
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

