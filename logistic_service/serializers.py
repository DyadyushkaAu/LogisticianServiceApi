from rest_framework import serializers
from .models import Logistician
from django.contrib.auth.models import User


class LogisticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistician
        fields = ('name', 'surname', 'lastname', 'logistlogin', 'logistpassword')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
