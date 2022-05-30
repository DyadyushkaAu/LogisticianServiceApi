from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('aboutus', views.About, name='about'),
    path('catalogue', views.Catalogue, name='catalogue'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup", views.signup, name="signup"),
    path('myorders', views.MyOrders, name='orders'),
    path('createorder', views.CreateOrder, name='crorder')
]
