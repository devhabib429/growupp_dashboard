# Generated by Django 4.1.2 on 2022-10-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_voucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='enrolment',
            field=models.CharField(default='Not Generated', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='payment_status',
            field=models.CharField(default='Null', max_length=20),
        ),
    ]