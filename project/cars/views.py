from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def car(request):
    all_car=Car.objects.order_by('-created_date')
    paginator=Paginator(all_car,4)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)

    model_search=Car.objects.values_list('model',flat=True).distinct()
    location_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    color_search=Car.objects.values_list('color',flat=True).distinct()
   
   
   
    context={
        'all_car':paged_cars,
        # 'search_fields':search_fields
        'model_search':model_search,
        'location_search':location_search,
        'year_search':year_search,
        'color_search':color_search
        

    }
    return render(request,'cars/car.html',context)



def car_details(request,id):
    single_car=get_object_or_404(Car,pk=id)
    print(single_car,'***********')
    context={
        'single_car':single_car,
    }
    return render(request,'cars/car_detail.html',context)




def search(request):
    cars=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    location_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    color_search=Car.objects.values_list('color',flat=True).distinct()
    condition_search=Car.objects.values_list('condition',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()
    if 'model' in request.GET:
        keyword=request.GET['model']
        if keyword:
            cars=cars.filter(model__icontains=keyword)
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)
    if 'location' in request.GET:
        keyword=request.GET['location']
        if keyword:
            cars=cars.filter(city__icontains=keyword)
    if 'Year' in request.GET:
        keyword=request.GET['Year']
        if keyword:
            cars=cars.filter(year__icontains=keyword)
    if 'Condition' in request.GET:
        keyword=request.GET['Condition']
        if keyword:
            cars=cars.filter(condition__icontains=keyword)
    if 'Transmission' in request.GET:
        keyword=request.GET['Transmission']
        if keyword:
            cars=cars.filter(transmission__icontains=keyword)
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if min_price and max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)

    
    context={
        'cars':cars,
        'model_search':model_search,
        'location_search':location_search,
        'year_search':year_search,
        'color_search':color_search,
        'condition_search':condition_search,
        'transmission_search':transmission_search,

    }

    return render(request,'cars/search.html',context)