# Generated by Django 4.1.2 on 2022-12-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_account_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='job_type',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]