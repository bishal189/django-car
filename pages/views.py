
from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


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
    all_cars=Car.objects.order_by('-created_date')[:1]
    context={
        'teams':teams,
        'all_cars':all_cars
    }
    return render(request,'pages/about.html',context)
def service(request):
    return render(request,'pages/service.html')
def contact(request):

    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']
        # email verification is not usable for now
    #     email_subject='You have a new message from carzone website regarding '+subject
    #     message_body='Name: '+name +' email: '+ email +' phone: '+phone + 'Message: '+ message
    #     admin_info= User.objects.get(is_superuser=True)
    #     admin_email=admin_info.email
    #     send_mail(
    #     email_subject,
    #     message_body,
    #     email,
    #    [admin_email],
    #    fail_silently=False,
    #              )

        messages.success(request,'Thanks you for contacting us.we will get back to your soon.')
        return redirect('contact')    ;     
       
    return render(request,'pages/contact.html')
   
def car(request):
    return render(request,'pages/car.html')
def help(request):
    return render(request,'pages/help.html')

