from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):

    if request.method == 'POST':
        car_id=request.POST['car_id']
        car_title=request.POST['car_title']
        user_id=request.POST['user_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        print(customer_need)
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        if request.user.is_authenticated:
            user_id=request.user.id;
            has_contact=Contact.objects.filter(car_id=car_id,user_id=user_id)
            if has_contact:
                messages.error(request,'you have already submited the query so wait for response')
                return redirect('/cars/'+car_id);

        contact=Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,
        last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)
        
        
    #   email verification is not usable for now
    #     admin_info=User.objects.get(is_superuser=True)
    #     admin_email=admin_info.email
    #     send_mail(
    #    'New car Inquiry',
    #    'You have a new inquiry for the car.'+ car_title+'please login to your admi panel for more info',
    #    'bishumurmu098@gmail.com',
    #    [admin_email],
    #    fail_silently=False,
    #              )

        contact.save()
        messages.success(request,'your request has been submited ,we will get back to you shortly')
        return redirect('/cars/'+car_id)
