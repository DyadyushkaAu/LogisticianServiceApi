# Generated by Django 4.0.4 on 2022-06-08 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic_service', '0010_rename_login_logistician_logislogin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logistician',
            old_name='logislogin',
            new_name='logistlogin',
        ),
    ]
