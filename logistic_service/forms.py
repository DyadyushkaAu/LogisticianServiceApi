from django import forms
from django.contrib.auth.models import User
from .models import Order, District, City, Street, Region
from django.forms import TextInput
import numbers

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean(self):
        cd = super().clean()

        if cd.get('password') != cd.get('password2'):
            self.add_error('password', 'Пароли не совпадают')


class OrdrsForm(forms.ModelForm):

    address = forms.CharField(max_length=255, required=False,
                              widget=forms.TextInput(attrs={
                                       'class': 'form-control'
                                   }))

    phone_number = forms.CharField(label='Введите номер телефона',
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Введите номер телефона'
                                   }))

    region = forms.ModelChoiceField(label='Выберите регион',
                                    queryset=Region.objects.all(),
                                    empty_label='Выберите регион',
                                    widget=forms.Select(
                                        attrs={'class': 'form-control'}
                                    )
                                    )

    city = forms.CharField(label='Выберите город',
                                      #choices=(('empty', 'Выберите город'),),
                                      widget=forms.Select(attrs={
                                          'class': 'form-control'
                                      }))

    district = forms.CharField(
        label='Выберите район обслуживания',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    street = forms.CharField(
        label='Выберите улицу',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ))

    desc = forms.CharField(label='Введите описание',
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Описание (необязательно)'
                                   }))

    home = forms.CharField(label='Введите номер дома',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Введите номер дома'
                           }))

    mass = forms.CharField(label='Введите массу',
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Введите массу'
                                   }))

    class Meta:
        model = Order
        fields = [
            # 'address',
            'mass', 'phone_number', 'orderer', 'state', 'description', 'district', 'street']
        widgets = {
            # 'address': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введите адрес'
            # }),
            # 'phone_number': CharField(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введите номер телефона'
            # }),
            # 'mass': TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Введите массу заказа'
            # })
        }

    def clean(self):
        cd = super().clean()

        print(cd.get('phone_number'), cd.get('address'), cd.get('mass'))

        if cd.get('phone_number') is None:
            self.add_error('phone_number', 'Введите номер телефона')
        if type(get_value_type(cd, 'phone_number')) != int:
            self.add_error('phone_number', 'Числовое значение пример: 89121545772')
        if cd.get('address') is None:
            self.add_error('address', 'Введите адресс')
        if type(cd.get('address')) != str:
            self.add_error('address', 'Текстовое значние')
        if cd.get('mass') is None:
            self.add_error('mass', 'Введите массу')
        if type(get_value_type(cd, 'mass')) != int:
            self.add_error('mass', 'Числовое значение')


def get_value_type(cd, key):
    try:
        return int(cd.get(key))
    except ValueError:
        return str
