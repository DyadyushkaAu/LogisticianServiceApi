from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Logistician(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    surname = models.CharField(max_length=80, null=False, blank=False)
    lastname = models.CharField(max_length=80, null=False, blank=False)
    logistlogin = models.CharField(max_length=80, null=False, blank=False)
    logistpassword = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Region(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    region = models.ForeignKey(Region, null=False,  blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id} {self.region.name} {self.name}'


class District(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id} {self.city.name} {self.name}'


class Street(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id} {self.name} {self.district.name}'


class Order(models.Model):
    address = models.CharField(max_length=150, null=False, blank=False)
    state = models.CharField(max_length=45, null=False, blank=True)
    date = models.DateField(auto_now_add=True)
    mass = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    phone_number = models.BigIntegerField(null=False, blank=False)
    orderer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    district = models.ForeignKey(District, null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f'{self.address} {self.state} {self.phone_number} {self.mass}'


class Manufacturer_Model(models.Model):
    manufacturer_model = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return f'{self.manufacturer_model}'


class Car(models.Model):
    gn = models.CharField(unique=True, max_length=10, primary_key=True)
    manufacturer_model = models.ForeignKey(Manufacturer_Model, on_delete=models.DO_NOTHING)
    max_weight = models.DecimalField(max_digits=10, decimal_places=1, null=False)

    def __str__(self):
        return f'{self.manufacturer_model} {self.gn}'


class Driver(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    surname = models.CharField(max_length=80, null=False, blank=False)
    lastname = models.CharField(max_length=80, null=False, blank=False)
    auto = models.ForeignKey(Car, null=False, blank=False, on_delete=models.DO_NOTHING)
    phone_number = models.BigIntegerField(null=False, blank=False)
    state = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return f'{self.name} {self.surname} {self.auto.manufacturer_model}|{self.auto.gn}'


class Waybill(models.Model):
    number_of_waybill = models.IntegerField(null=False, blank=False)
    state = models.CharField(max_length=45, null=False, blank=False)
    district = models.ForeignKey(District, null=False, blank=False, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey(Driver, null=False, blank=False, on_delete=models.DO_NOTHING)
    logistician = models.ForeignKey(Logistician, null=False, blank=False, on_delete=models.DO_NOTHING)
    registration_date = models.DateField(auto_now_add=True, null=False, blank=False)
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.DO_NOTHING)
    state = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return f'{self.number_of_waybill} {self.order.address} {self.state}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='????????????????????????')
    phone_number = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.phone_number}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
