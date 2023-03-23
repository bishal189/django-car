
from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.


def home(request):
    teams=Team.objects.all()
    car_feature=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')
    # search_fields=Car.objects.values('model','city','year','color')
   
    model_search=Car.objects.values_list('model',flat=True).distinct()
    location_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    color_search=Car.objects.values_list('color',flat=True).distinct()
   
   
    
   
    
    context={
        'teams':teams,
        'car_feature':car_feature,
        'all_car':all_car,
        # 'search_fields':search_fields
        'model_search':model_search,
        'location_search':location_search,
        'year_search':year_search,
        'color_search':color_search
        
        
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

