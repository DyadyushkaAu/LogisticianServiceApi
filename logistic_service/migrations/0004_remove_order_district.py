# Generated by Django 4.0.4 on 2022-06-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic_service', '0003_order_city_order_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='district',
        ),
    ]