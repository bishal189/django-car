
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('car/',views.car,name='car'),
    path('help/',views.help,name='help'),
]
