# Generated by Django 5.1.1 on 2024-11-12 20:07

import petstagram_2024.accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', petstagram_2024.accounts.managers.AppUserManager()),
            ],
        ),
    ]