from rest_framework import serializers
from .models import Logistician
from django.contrib.auth.models import User


class WayBillSerializer(serializers.Serializer):
    # number_of_waybill = serializers.IntegerField()
    number_of_waybill = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=45)
    # district = serializers.IntegerField()
    district = serializers.CharField(max_length=255)
    # driver = serializers.IntegerField()
    driver = serializers.CharField(max_length=255)
    # logistician = serializers.IntegerField()
    logistician = serializers.CharField(max_length=255)
    registration_date = serializers.DateField()
    # order = serializers.IntegerField()
    order = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=45)


