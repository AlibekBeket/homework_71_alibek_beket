# Generated by Django 4.1.7 on 2023-03-27 22:35

import accounts.managers
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('object', accounts.managers.UserManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
