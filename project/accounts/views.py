from django.shortcuts import render
from contact.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are login!')
            return redirect('dashboard')


        else:
            messages.error(request,'invalid login credentials');
            return redirect('login')    

    return render(request,'accounts/login.html')
def register(request):
    if request.method == 'POST':
       first_name=request.POST['firstname']
       last_name=request.POST['lastname']
       user_name=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       confrim_password=request.POST['confirm_password']


       if password == confrim_password:
        if User.objects.filter(username=user_name).exists():
            messages.error(request,'username already exist!')
            return redirect('register')


        else:
            if User.objects.filter(email=email).exists():
                messages.error(request,'email already exists!')
                return redirect('register')

            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password)
                auth.login(request,user)
                messages.success(request,'You are loged in!')
                return redirect('dashboard')
                user.save()
                messages.success(request,'You are registired sucessfully!')
                return redirect('login')



                                                          
        
        

       else:

        messages.error(request,'Password do not match')
        return render(request,'accounts/register.html') 
    else:
        return render(request,'accounts/register.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
@login_required(login_url='login')    
def dashboard(request):
    user_inquiry=Contact.objects.order_by('create_date').filter(user_id=request.user.id)
    data={
        'inquiry':user_inquiry,
    }
    
    return render(request,'accounts/dashboard.html',data)
