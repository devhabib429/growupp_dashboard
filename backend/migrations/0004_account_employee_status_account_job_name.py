# Generated by Django 4.1.2 on 2022-12-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_account_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='employee_status',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='job_name',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]
