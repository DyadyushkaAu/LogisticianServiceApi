# Generated by Django 4.0.4 on 2022-06-08 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic_service', '0009_remove_driver_user_remove_logistician_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logistician',
            old_name='login',
            new_name='logislogin',
        ),
        migrations.RenameField(
            model_name='logistician',
            old_name='password',
            new_name='logistpassword',
        ),
    ]
