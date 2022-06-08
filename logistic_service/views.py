from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from rest_framework.response import Response

from .forms import UserRegistrationForm, OrdrsForm
from .models import Order, City, Street, District, Region, Logistician
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView

from .serializers import LogisticianSerializer, UserSerializer


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
            form.address = f'{request.POST["city"]}, {request.POST["street"]}, {request.POST["home"]}'
            form.description = f'{request.POST["desc"]}'
            form.state = 'Новый'
            form.district = District.objects.get(id=request.POST["district"])
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


class LogisticianApiView(generics.ListAPIView):
    queryset = Logistician.objects.all()
    serializer_class = LogisticianSerializer

    # def get(self):
    #     return Logistician.objects.get(id=1).user.username


class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # usernames = []
        queryset = Logistician.objects.all()
        #     usernames.append([{logist.logistlogin} {logist.logistpassword}])
        return Response(LogisticianSerializer)

    def post(self, request):
        return Response('"status": "ZAEBIS"')
