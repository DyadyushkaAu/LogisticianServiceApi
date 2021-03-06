# Generated by Django 4.0.4 on 2022-06-05 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic_service', '0002_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='logistic_service.district'),
            preserve_default=False,
        ),
    ]
