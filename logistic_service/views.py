from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm, OrdrsForm
from .models import Order, City, Street, District, Region


def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'logistic_service/register_done.html', context={
                'new_user': new_user,
                'title': 'Регистрация завершена'
            })
        else:
            user_form = UserRegistrationForm(request.POST)
            return render(request, 'logistic_service/signup.html', context={
                'user_form': user_form,
                'title': 'Регистрация'
            })
    else:
        user_form = UserRegistrationForm()
        return render(request, 'logistic_service/signup.html', context={
            'user_form': user_form,
            'title': 'Регистрация'
        })


def Index(request):
    print('ffff')
    return render(request, 'logistic_service/index.html')


def About(request):
    return render(request, 'logistic_service/AboutUs.html')


def Catalogue(request):
    return render(request, 'logistic_service/catalogue.html')


def MyOrders(request):
    orders = Order.objects.filter(orderer=request.user)
    cities = City.objects.all()
    streets = Street.objects.all()
    districts = District.objects.all()
    return render(request, 'logistic_service/orders.html', {
        'orders': orders,
        'cities': cities,
        'streets': streets,
        'districts': districts,
        'user': request.user
    })


def CreateOrder(request):
    error = ''
    if request.method == 'POST':
        print(request.POST)
        form = OrdrsForm(request.POST)
        if form.is_valid():
            print('BFIDBIFBIDBFI')
            form = form.save(commit=False)
            form.orderer = request.user
            form.address = f'{request.POST["street"]}, {request.POST["home"]}'
            form.state = 'Новый'
            form.save()
            return render(request, 'logistic_service/order_ready.html')
        else:
            print(form.errors)
            form = OrdrsForm(request.POST)
            return render(request,
                          'logistic_service/createorder.html',
                          context={'form': form, 'error': 'Форма неверна'})

    form = OrdrsForm()
    regions = Region.objects.all()
    cities = City.objects.all()
    districts = District.objects.all()
    streets = Street.objects.all()
    context = {
        'form': form,
        'error': error,
        'regions': regions,
        'cities': cities,
        'districts': districts,
        'streets': streets

    }
    return render(request, 'logistic_service/createorder.html', context)
